from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import User
from utils.response import errorResponse,successResponse
from utils.jwt import sendToken
from utils.authenticate import isAuthenticated

class RegisterView(APIView):
    def post(self,req):
        user =User.objects.filter(email=req.data["email"]).first()
        if user :
            return errorResponse("User Already Exists...!",400)
        serializer = UserSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
        return successResponse(serializer.data,"User Created SuccessFully...!",201)

class LoginView(APIView):
    def post(self,req):
        email = req.data["email"]
        password = req.data["password"]
        user = User.objects.filter(email=email).first()
        if user is None :
            return errorResponse("Invalid Credentials...!",400)
        if not user.check_password(password):
            return errorResponse("Invalid Credentials...!",400)
        return sendToken(user)

class LogoutView(APIView):
    def put(self,req):
        req = isAuthenticated(req)
        if req is None : return errorResponse("Login To View",403)
        response = successResponse({},"User Logged Out Successfully...!",201)
        response.delete_cookie(key="token")
        return response
 
