from django.urls import path
from .views import create_person, create_person_model_form

urlpatterns = [
   path('cp-form/', create_person, name="create_person"),
   path('cp-model-form/', create_person_model_form, name="create_person_model_form")
]