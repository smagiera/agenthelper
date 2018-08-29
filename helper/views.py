from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404,render
from django.urls import reverse,reverse_lazy
from django.views import generic
from django import forms
from datetime import date,timedelta
from dal import autocomplete
from django.db.models import Sum

from .models import Policy, Vehicle, Client
from .forms import PolicyForm, VehicleForm, ClientForm, InsurerForm


class IndexView(generic.ListView):
    template_name = 'helper/index.html'
    context_object_name = 'policy_list'

    def get_queryset(self, start_date = date.today() - timedelta(days=1), end_date=date.today()):
        """Return all policies in specified timeframe"""
        return Policy.objects.filter(date_issued__range=(start_date, end_date+timedelta(days=1)))

class PolicyList(generic.ListView):
    template_name = 'helper/policy_list.html'
    context_object_name = 'policy_list'

    def get_queryset(self):
        """Return all policies in specified timeframe"""
        date_from = self.kwargs['datefrom']
        date_to = self.kwargs['dateto']
        return Policy.objects.filter(date_issued__range=(date_from, date_to))

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
    form_class = VehicleForm
    template_name = 'helper/vehicle_form.html'

class VehicleUpdate(generic.UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'helper/vehicle_form.html'

class VehicleDelete(generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy('helper:vehicles')

class ClientList(generic.ListView):
    template_name = 'helper:client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        """Return all clients"""
        return Client.objects.all()

class ClientDetail(generic.DetailView):
    model = Client
    template_name = 'helper/client_details.html'

class ClientCreate(generic.CreateView):
    form_class = ClientForm
    template_name = 'helper/client_form.html'

class ClientUpdate(generic.UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'helper/client_form.html'

class ClientDelete(generic.DeleteView):
    model = Client
    success_url = reverse_lazy('helper:clients')

class InsurerCreate(generic.CreateView):
    form_class = InsurerForm
    template_name = 'helper/insurer_form.html'
    success_url = reverse_lazy('helper:index')

class StatisticsView(generic.TemplateView):
    template_name = 'helper/statistics.html'
    context_object_name = 'context'

    def count_policies(self):
        return Policy.objects.count()
    
    def przypis(self):
        return Policy.objects.aggregate(Sum('premium'))['premium__sum']


class ClientAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Client.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        
        return qs

class VehicleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Vehicle.objects.all()
        if self.q:
            qs = qs.filter(reg_number__icontains=self.q)
        
        return qs
