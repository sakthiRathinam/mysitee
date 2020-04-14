
from django.urls import path,include
from .views import home,signup,form

urlpatterns = [
    path('home/',home,name="home"),
   	path('form/',form,name="form"),
    path('signup/',signup,name="signup"),
]
