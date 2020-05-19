from django.urls import path
from annonce import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('all_obj_api', views.obj_list.as_view()),
    path('obj_api/<int:pk>', views.obj_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
