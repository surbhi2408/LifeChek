from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('diabetes/',diabetes,name='diabetes'),
    path('breast/',breast,name='breast'),
    path('heart/',heart,name='heart'),
    path('lung_cancer/',lung_cancer,name='lung_cancer'),
]
