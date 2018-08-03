from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django import forms

from .models import Policy, Vehicle
from .forms import PolicyForm, VehicleForm


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

class VehicleList(generic.ListView):
    template_name = 'helper:vehicle_list.html'
    context_object_name = 'vehicle_list'

    def get_queryset(self):
        """Return all vehicles"""
        return Vehicle.objects.all()

class VehicleDetail(generic.DetailView):
    model = Vehicle
    template_name = 'helper/vehicle_details.html'

class VehicleCreate(generic.CreateView):
    model = Vehicle
    template_name = 'helper/vehicle_form.html'

class VehicleUpdate(generic.UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'helper/vehicle_form.html'

class VehicleDelete(generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy('helper:vehicles')