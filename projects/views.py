# Create your views here.
from django.views.generic import ListView

from projects.models import Project, Donation


class ProjectsList(ListView):
    queryset = Project.objects.all()
    template_name = "index.html"


class DonationList(ListView):
    template_name = "donation_list.html"

    def get_queryset(self):
        return Donation.objects.filter(project__pk=self.kwargs['pk'])
