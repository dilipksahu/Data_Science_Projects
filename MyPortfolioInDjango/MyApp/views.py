from django.shortcuts import render
from .models import MySkill,Service,Portfolio

# Create your views here.
def home(request):
    skills = MySkill.objects.all()
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    data = {
        'skills':skills,
        'services':services,
        'portfolios':portfolios,
    }
    return render(request,'base.html',data)

