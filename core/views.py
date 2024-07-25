from django.shortcuts import render, redirect
from core.models import Resource
from core.forms import NewsletterForm
from django.contrib import messages

def index(request):
    resources = Resource.objects.all()

    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Welcome to the club!')
        return redirect('index')

    return render(request, 'core/index.html', {'resources': resources, 'form': form})
