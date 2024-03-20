# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms


def emailView(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contactus/email.html", {'form': form})


def successView(request):
    return render(request, 'contactus/thankyou.html')
