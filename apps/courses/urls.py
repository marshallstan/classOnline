# __author__ = 'Marshall Stan'

from django.conf.urls import url
from .views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
]
