from django.urls import path,include
from  .views import CreateProductView,FetchProductsView,DeleteProductView,FetchProductView,UpdateProductView


urlpatterns = [
    path("create-product/",CreateProductView.as_view()),
    path("fetch-products/",FetchProductsView.as_view()),
    path("fetch-product/<int:id>/",FetchProductView.as_view()),
    path("update-product/<int:id>/",UpdateProductView.as_view()),
    path("delete-product/<int:id>/",DeleteProductView.as_view())
]
