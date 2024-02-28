from django.shortcuts import render
from rest_framework.views import APIView
from utils.authenticate import isAuthenticated,isAdmin
from utils.response import errorResponse,successResponse
from .serailizers import ProductSerializer
from .models import Product

class CreateProductView(APIView):
    def post(self,req):

        req = isAuthenticated(req)
        if req is None : return errorResponse("Login to View...!",403)
        admin = isAdmin(req.user)
        if not admin : return errorResponse("Only Admins Are Allowed...!",403)
        
        serializer = ProductSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse(serializer.data,"Product Created Successfully...!",201)


class FetchProductsView(APIView):
    def get(self,req):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return successResponse(serializer.data,"Products Fetched Successfully...!",200)

class FetchProductView(APIView):
    def get(self,req,id):
        product = Product.objects.filter(id=id).first()
        serializer = ProductSerializer(product,many=False)
        return successResponse(serializer.data,"Products Fetched Successfully...!",200)

class UpdateProductView(APIView):
    def put(self,req,id):

        req = isAuthenticated(req)
        if req is None : return errorResponse("Login to View...!",403)
        admin = isAdmin(req.user)
        if not admin : return errorResponse("Only Admins Are Allowed...!",403)

        product =Product.objects.filter(id=id).first()
        if product is None : return errorResponse("Product Doesn't Exits...!",403)
        serializer = ProductSerializer(instance=product,data=req.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return successResponse(serializer.data,"Product Updated Successfully...!",201)

class DeleteProductView(APIView):
    def delete(self,req,id):

        req = isAuthenticated(req)
        if req is None : return errorResponse("Login to View...!",403)
        admin = isAdmin(req.user)
        if not admin : return errorResponse("Only Admins Are Allowed...!",403)

        product =Product.objects.filter(id=id).first()
        if product is None : return errorResponse("Product Doesn't Exits...!",403)
        serializer = ProductSerializer(product,many=False)
        product.delete()
        return successResponse(serializer.data,"Product Deleted Successfully...!",201)