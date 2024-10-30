from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import *
# authentication/views.py



def home(request):
    return render(request, 'home.html')

def projects(request):
    
    pro = {
        'projects' : Projects.objects.all(),
    
    }
    
    return render(request, 'projects.html', pro)

def about_me(request):
    return render(request, 'about_me.html')

def contact_me(request):
    return render(request, 'contact_me.html')

def services(request):
    return render(request, 'service.html')


def image(request):
    return render(request, 'image.html')



def buy(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or perform further actions
            return redirect('success_page')
    else:
        form = OrderForm()

    return render(request, 'buy.html', {'form': form})


def order_done(request):
    return render(request, 'order_done.html')


