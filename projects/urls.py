from django.urls import path

from projects.views import ProjectsList, DonationList

urlpatterns = [
    path("", ProjectsList.as_view(), name="index"),
    path("donations/<pk>", DonationList.as_view(), name="donations"),
]
