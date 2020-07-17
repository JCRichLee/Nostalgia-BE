from django.shortcuts import render
from django.http import HttpResponse
from .models import * 
from .forms import EmailsForm

# Create your views here.

def index(request):
    form = EmailsForm()

    if request.POST:
        form = EmailsForm(request.POST)
        if form.is_valid():
           author = form.save()

        else:
            print ('error!')

    context = {
        'form': form,
    }

    return render(request, 'emailapp/index.html',context)