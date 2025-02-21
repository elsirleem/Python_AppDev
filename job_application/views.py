from django.shortcuts import render
from .forms import JobApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data["firstname"]
            lastname = form.cleaned_data["lastname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                date=date,
                occupation=occupation
            )

            message_body = f"A new job application has been submitted by {firstname} {lastname}."
            email_message = EmailMessage("Form Submission", message_body, to=[email])
            email_message.send()
            messages.success(request, "Form submitted successfully")
    return render(request, "index.html")
