from django.urls import path
from . import views 


urlpatterns = [
    path('studentapi/',views.StudentList.as_view()),
]

