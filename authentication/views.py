from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.backends import UserModel
from user.forms import RegistrationForm

@csrf_exempt
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            "current_user": request.user,
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)


def logout_user(request):
    logout(request)
    return JsonResponse({
        "status": False,
        "message": "Successfully logged out"
    }, status=200)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        email = data["email"]
        username = data["username"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        password1 = data["password1"]
        password2 = data["password2"]
        user_role = data["user_role"]

        form = RegistrationForm(request.POST)

        if UserModel.objects.filter(username=username).exists():
            return JsonResponse({"status": "duplicate"}, status=401)

        if password1 != password2:
            return JsonResponse({"status": "pass failed"}, status=401)

        if form.is_valid():
            form.save()
            return JsonResponse({
                "status": True,
                'message': 'User successfully registered',
            }, status=200)
        return JsonResponse({
            "status": False,
            'message': 'Something went wrong',
        }, status=400)

        # createNewUser = UserModel.objects.create_user(
        # username = username, 
        # password = password1,
        # )
        # createNewUser.save()