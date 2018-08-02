from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views import generic

from .models import Policy, Vehicle

class IndexView(generic.ListView):
    template_name = 'helper/index.html'
    context_object_name = 'policy_list'

    def get_queryset(self):
        """Return 10 last issued policies"""
        return Policy.objects.order_by('-date_issued')[:10]

class DetailView(generic.DetailView):
    model = Policy
    template_name = 'helper/details.html'