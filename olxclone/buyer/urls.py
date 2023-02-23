from django.contrib import admin
from django.urls import path,include
from buyer import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path("",views.SignInView.as_view(),name="signin"),
    path("register",views.SignUpView.as_view(),name="signup"),
    path("home",views.HomeView.as_view(),name="home"),
    path("productadd",views.product_create,name="add-product"),
    path("products/details/<int:id>",views.ProductDetailView.as_view(),name="product-detail"),
    path('profile',views.ViewProfile.as_view(),name='profile'),
    path('viewprofile',views.profile_create,name="view"),
    path("myproducts",views.MyProductView.as_view(), name="my-product"),
    path("chat",views.ChatView.as_view(), name="chat"),


]