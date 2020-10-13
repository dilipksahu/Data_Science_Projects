from django.shortcuts import render
from .models import MySkill,Service

# Create your views here.
def home(request):
    skills = MySkill.objects.all()
    services = Service.objects.all()
    data = {
        'skills':skills,
        'services':services,
    }
    return render(request,'base.html',data)

# def myskill(request):
#     skills = MySkill.objects.all()
#     data = {
#         'skills':skills,
#     }
#     return render(request,'base.html',data)

# def myservices(request):
#     services = Service.objects.all()
#     data = {
#         'services':services,
#     }
#     return render(request,'base.html',data)