from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.response import Response
#
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny

from account.models import Customuser


def homepage(request):
    return render(request, template_name="home.html", context={})


def register(request):
    user = Customuser.objects.filter(first_name=request.POST.get("first_name")).first()
    if user:
        return render(request, template_name="home.html", context={"error": "user exits"})
    user = User.objects.create(
        first_name=request.POST.get("first_name"),
        last_name=request.POST.get("last_name"),
        gender=request.data.get('gender'),
        birth_date=request.data.get('birth_date'),
        region=request.data.get('region'),
        city=request.data.get('city')
    )
    user.save()

    return render(request,template_name="base.html")
    # else:
    #     return render(request, template_name="home.html", context={"error": "Password error"})

# def registr(request):
#     try:
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         gender = request.data.get('gender')
#         birth_date = request.data.get('birth_date')
#         region = request.data.get('region')
#         city = request.data.get('city')
#         user = request.user
#         user.first_name = first_name
#         user.last_name = last_name
#         user.gender = gender
#         user.birth_date = birth_date
#         user.region_id = region
#         user.city_id = city
#         if 'avatar' in request.data:
#             user.avatar = request.data['avatar']
#         user.save()
#         return Response()
#     except KeyError:
#         res = {
#             'status': 0,
#             'msg': 'Please set all reqiured fields'
#         }
#         return Response(res)
