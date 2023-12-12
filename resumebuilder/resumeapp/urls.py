# urls.py
from django.urls import path
from .views import GeneratePDF

urlpatterns = [
    path('user_form/', GeneratePDF.as_view(), name='user_form'),

]
