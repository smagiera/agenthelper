from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse,reverse_lazy
from django.views import generic
from django import forms
from datetime import date,timedelta
from dal import autocomplete
from django.db.models import Sum

from .models import Policy, Vehicle, Client, Insurer
from .forms import PolicyForm, VehicleForm, ClientForm, InsurerForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'helper/index.html'
    context_object_name = 'policy_list'

    def get_queryset(self, start_date = date.today() - timedelta(days=1), end_date=date.today()):
        """Return all policies in specified timeframe"""
        return Policy.objects.filter(date_issued__range=(start_date, end_date+timedelta(days=1)))

class PolicyList(LoginRequiredMixin, generic.ListView):
    template_name = 'helper/policy_list.html'
    context_object_name = 'policy_list'

    def get_queryset(self):
        """Return all policies in specified timeframe"""
        date_from = self.kwargs['datefrom']
        date_to = self.kwargs['dateto']
        return Policy.objects.filter(date_issued__range=(date_from, date_to), agent=self.request.user)

class AllPolicyList(LoginRequiredMixin, generic.ListView):
    template_name = 'helper/policy_list.html'
    context_object_name = 'policy_list'

    def get_queryset(self):
        """Return all policies in specified timeframe"""
        date_from = self.kwargs['datefrom']
        date_to = self.kwargs['dateto']
        return Policy.objects.filter(date_issued__range=(date_from, date_to))

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Policy
    template_name = 'helper/details.html'

class PolicyCreate(LoginRequiredMixin, generic.CreateView):
    form_class = PolicyForm
    template_name = 'helper/policy_form.html'
    def get_initial(self):
        return {
            'agent': self.request.user
        }

class PolicyUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Policy
    form_class = PolicyForm
    template_name = 'helper/policy_form.html'

class PolicyDelete(LoginRequiredMixin, generic.DeleteView):
    model = Policy
    success_url = reverse_lazy('helper:index')

class VehicleList(LoginRequiredMixin, generic.ListView):
    template_name = 'helper:vehicle_list.html'
    context_object_name = 'vehicle_list'

    def get_queryset(self):
        """Return all vehicles"""
        return Vehicle.objects.all()

class VehicleDetail(LoginRequiredMixin, generic.DetailView):
    model = Vehicle
    template_name = 'helper/vehicle_details.html'

class VehicleCreate(LoginRequiredMixin, generic.CreateView):
    form_class = VehicleForm
    template_name = 'helper/vehicle_form.html'

class VehicleUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'helper/vehicle_form.html'

class VehicleDelete(LoginRequiredMixin, generic.DeleteView):
    model = Vehicle
    success_url = reverse_lazy('helper:vehicles')

class ClientList(LoginRequiredMixin, generic.ListView):
    template_name = 'helper:client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        """Return all clients"""
        return Client.objects.order_by('name')

class ClientDetail(LoginRequiredMixin, generic.DetailView):
    model = Client
    template_name = 'helper/client_details.html'
    def all_his_policies(self):
        """Returns all policies for a given client"""
        return Policy.objects.filter(client=self.object.id)

class ClientCreate(LoginRequiredMixin, generic.CreateView):
    form_class = ClientForm
    template_name = 'helper/client_form.html'
    
    def clean(self):
        if self._meta.model.objects.filter(**self.cleaned_data).count() > 0:
            raise forms.ValidationError('Client already exists')
        return self.cleaned_data

class ClientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'helper/client_form.html'

class ClientDelete(LoginRequiredMixin, generic.DeleteView):
    model = Client
    success_url = reverse_lazy('helper:clients')

class InsurerCreate(LoginRequiredMixin, generic.CreateView):
    form_class = InsurerForm
    template_name = 'helper/insurer_form.html'
    success_url = reverse_lazy('helper:index')

class InsurerList(LoginRequiredMixin, generic.ListView):
    template_name = 'helper:insurer_list.html'
    context_object_name = 'insurer_list'

    def get_queryset(self):
        """Return all insurers"""
        return Insurer.objects.all()


class StatisticsView(LoginRequiredMixin, generic.TemplateView):
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


class SignupView(generic.FormView):
    template_name = 'helper/signup.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('helper:index')

