
from django.urls import path,include
from .views import home,signup,form,createOrder,updateOrder,deleteOrder

urlpatterns = [
    path('home/',home,name="home"),
   	path('form/',form,name="form"),
    path('signup/',signup,name="signup"),
    path('update/<str:name>',updateOrder,name='update'),
    path('delete/<str:name>',deleteOrder,name='delete'),
    path('create/',createOrder,name="create"),
]
