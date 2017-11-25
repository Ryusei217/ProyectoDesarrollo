from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from two_factor.utils import default_device


@login_required
def home(request):
    return render(request, 'home.html', {'default_device': default_device(request.user)})
