from django.urls import path
from .views import create_person, create_person_model_form, CreatePersonView, PersonListView, PersonDetailView
# from django.contrib.auth.decorators import login_required

urlpatterns = [
   path('cp-form/', create_person, name="create_person"),
   path('cp-model-form/', create_person_model_form, name="create_person_model_form"),
   # path('cp-views/', login_required(CreatePersonView.as_view()), name="cp_views"),
   path('cp-views/', CreatePersonView.as_view(), name="cp_views"),
   path('person-list/', PersonListView.as_view(), name="person_list"),
   path('person-detail/<int:id>/', PersonDetailView.as_view(), name="person_detail_view"),
]