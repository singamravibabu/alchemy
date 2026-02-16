from django.urls import path
from .views import CourseList, CourseDetail, CourseCreate, CourseUpdate, CourseDelete

urlpatterns = [
    path("course-list/", CourseList.as_view()),
    path("course-detail/<int:pk>/", CourseDetail.as_view()),
    path('course-create/', CourseCreate.as_view()),
	path('course-update/<int:pk>/', CourseUpdate.as_view()),
	path('course-delete/<int:pk>/', CourseDelete.as_view()),
]