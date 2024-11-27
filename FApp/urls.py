from django.urls import path
from FApp import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),

    path('add_category/',views.add_category,name="add_category"),
    path('save_category/',views.save_category,name="save_category"),
    path('view_category/',views.view_category,name="view_category"),
    path('edit_category/<int:c_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:c_id>/',views.update_category,name="update_category"),
    path('delete_category/<int:c_id>/',views.delete_category,name="delete_category"),

    path('add_product/', views.add_product, name="add_product"),
    path('save_product/', views.save_product, name="save_product"),
    path('view_product/', views.view_product, name="view_product"),
    path('edit_product/<int:c_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:c_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:c_id>/', views.delete_product, name="delete_product"),

    path('login_page/', views.login_page, name="login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),


    path('contactdetails/', views.contactdetails, name="contactdetails"),






]