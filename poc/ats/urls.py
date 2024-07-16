from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("", views.ApplicantView, basename="applicant-view")


urlpatterns = [
    path('search/', views.ApplicantSortedView.as_view(), name='applicant-view'),
    *router.urls,
]
