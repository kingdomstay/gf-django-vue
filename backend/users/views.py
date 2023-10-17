import logging

from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .forms import ProfileEditForm, UserEditForm
from .models import Profile
from .serializers import ProfileSerializer

Logger = logging.getLogger("main")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# profile = Profile.objects.create(user=new_user)

# @login_required
# def edit(request):
#     if request.method == "POST":
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#         return render(request, "account/edit.html", {"user_form": user_form, "profile_form": profile_form})

def login_view(request):
    Logger.info("Получен")
    return HttpResponse("<h1>Hello</h1>")