from django.shortcuts import render
import pyrebase
#import djfrontend
from django.urls import include, re_path

config = {
    'apiKey': "AIzaSyC-WYZzWmRAbTcxOVP0By-veAwqaEECKyI",
    'authDomain': "officemanagement-9380b.firebaseapp.com",
    'databaseURL': "https://officemanagement-9380b.firebaseio.com",
    'projectId': "officemanagement-9380b",
    'storageBucket': "officemanagement-9380b.appspot.com",
    'messagingSenderId': "739901980799"
  }
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


def signIn(request):
    return render(request, "signIn/signIn.html")


def postSign(request):

    email = request.POST.get('email')
    password = request.POST.get('password')

    try:
        user = auth.sign_in_with_email_and_password(email, password)

    except:
        message = "Invalid Credentials"
        return render(request, "signIn/signIn.html", {"messg": message})

    if email.endswith("@order.com"):
        return render(request, "signIn/authenticate.py", {"e": email})
    elif email.endswith("@barcode.com"):
        return render (request, "signIn/barcode.html")
    elif email.endswith("@admin.com"):
        return render(request, "signIn/option.html")
    elif email.endswith("@billing.com"):
        return render(request, "signIn/billing.html")