from django.urls import path
from user import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('all_obj_api_c', views.obj_list_c.as_view()),
    path('obj_api_c/<int:pk>', views.obj_details_c.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
