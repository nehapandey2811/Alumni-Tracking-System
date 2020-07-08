from django.shortcuts import render

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

class SendFormEmail(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)
        message = request.GET.get('message', None)

        send_mail(
            'Subject- Django Email Testing', 
            'Hello ',
            'nehasamala153@gmail.com', # Admin
            [
                email,
            ]
        )

        

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('/')