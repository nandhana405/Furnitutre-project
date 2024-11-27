from django.urls import path
from newapp import views

urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('aboutpage/',views.aboutpage,name="aboutpage"),
    path('contactpage/',views.contactpage,name="contactpage"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('shoppage/<cat_name>/',views.shoppage,name="shoppage"),
    path('singleproduct/<int:pro_id>/',views.singleproduct,name="singleproduct"),
    path('blogpage/',views.blogpage,name="blogpage"),
    path('signuppage/',views.signuppage,name="signuppage"),
    path('',views.signinpage,name="signinpage"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('Userlogout/',views.Userlogout,name="Userlogout"),
    path('save_cart/',views.save_cart,name="save_cart"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('deletecart/<int:d_id>/',views.deletecart,name="deletecart"),
    path('chechoutpage/',views.chechoutpage,name="chechoutpage"),
    path('save_order/',views.save_order,name="save_order"),
    path('paymentpage/',views.paymentpage,name="paymentpage"),

    ]