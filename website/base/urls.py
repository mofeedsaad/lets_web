from django.urls import path
from . import views


urlpatterns=[

    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logot/',views.logoutUser,name="logout"),
    path('',views.home,name="home"),
    path('user/',views.userPage,name="user-page"),
    path('products/',views.products),
    path('customer/',views.customer),
    path('product_detail/',views.product_detail,name="product_detail"),
    path('search/', views.search, name='search'),

    
]