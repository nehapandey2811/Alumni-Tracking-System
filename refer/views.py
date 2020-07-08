from django.shortcuts import render

from django.views.generic import View
from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail

class SendFormEmail1(View):

    def  get(self, request):

        # Get the form data 
        name = request.GET.get('name', None)
        email = request.GET.get('email', None)

        send_mail(
            'Subject- Django Email Testing', 
            'we have created an alumni app.you can be a part of that group.for further details go to www.alumni.com ',
            'nehasamala153@gmail.com', # Admin
            [
                email,
            ]
        )

        

        # Redirect to same page after form submit
        messages.success(request, ('Email sent successfully.'))
        return redirect('/')