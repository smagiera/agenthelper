from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django import forms

from .models import Policy, Vehicle
from .forms import PolicyForm


class IndexView(generic.ListView):
    template_name = 'helper/index.html'
    context_object_name = 'policy_list'

    def get_queryset(self):
        """Return 10 last issued policies"""
        return Policy.objects.order_by('-date_issued')[:10]

class DetailView(generic.DetailView):
    model = Policy
    template_name = 'helper/details.html'

class PolicyCreate(generic.CreateView):
    form_class = PolicyForm
    template_name = 'helper/policy_form.html'

class PolicyUpdate(generic.UpdateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'helper/policy_form.html'

class PolicyDelete(generic.DeleteView):
    model = Policy
    success_url = reverse_lazy('helper:index')