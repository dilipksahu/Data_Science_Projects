from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquary(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id,car_id=car_id)
            if has_contacted:
                messages.error(request,"You have already made an inquary about this car. please wait until we get bact to you.")
                return redirect('/cars/'+car_id)

        contact = Contact(first_name=first_name,last_name=last_name,car_id=car_id,
        customer_need=customer_need,car_title=car_title,city=city,state=state,
        email=email,phone=phone,message=message,user_id=user_id)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                'New Car Inquary',
                'You have a new inquary for the car '+ car_title +' .Please check your admin panel for more info.',
                'sahudil418@gmail.com',
                [admin_email],
                fail_silently=False,
                )

        contact.save()
        messages.success(request,"You request have been submitted. We will get back to you shortly.")
        return redirect('/cars/'+car_id)
