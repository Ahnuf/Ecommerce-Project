from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect


def login_page(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "Your Account is not verified")
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email, password = password)
        if user_obj.exists():
            login(request, user_obj)
            return redirect('/')
        
        messages.warning(request, "Invalid Credentials.")
        return HttpResponseRedirect(request.path_info)
    return render(request, "accounts/login.html")

def signup_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, "User Already Exists")
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email,
            )
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "An E-mail has been sent.")
        return HttpResponseRedirect(request.path_info)

    return render(request, "accounts/register.html")