from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Policy

# Create your views here.

def index(request):
    policy_list = Policy.objects.order_by('-date_issued')[:10]
    context = {
        'policy_list': policy_list,
    }
    return render(request, 'helper/index.html', context)

def details(request, policy_id):
    policy = get_object_or_404(Policy, pk=policy_id)
    return render(request, 'helper/details.html', {'policy': policy})