from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import status, mixins, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
#
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings
from rest_framework_jwt.settings import api_settings
from account.models import Customuser, Region
from account.serializer import CustomuserSerializer, RegionListSerializer

#
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Customuser.objects.all()
    serializer_class = CustomuserSerializer
    # pagination_class = LargeResultsSetPagination
    filter_backends = [ filters.SearchFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name']

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

    return render(request, template_name="base.html")
    # else:
    #     return render(request, template_name="home.html", context={"error": "Password error"})


@api_view(['GET'])
@permission_classes([AllowAny, ])
def region(request):
    region_id = request.GET.get("region_id")
    if region_id:
        region_id = Region.objects.filter(parent_id=region_id).all()
    else:
        region_id = Region.objects.filter(parent__isnull=True).all()

    res = {
        'status': 1,
        'data': RegionListSerializer(region_id, many=True, context={"request": request}).data,
    }
    return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def registr(request):
    try:
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        phone = request.data.get('phone')
        gender = request.data.get('gender')
        region = request.data.get('region')
        city = request.data.get('city')
        birth_date = request.data.get('birth_date')
        passport = request.data.get('passport')

        user = Customuser.objects.filter(username=first_name).first()
        if not user:
            if 'avatar' in request.data:
                user.avatar = request.data['avatar']
                user.save()
            user = Customuser.objects.create(
                username=first_name,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                gender=gender,
                region_id=region,
                city_id=city,
                birth_date=birth_date,
                passport=passport,
                email=email,
                complete=1
            )

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
        elif user:
            res = {
                'msg': 'User exits',
                'status': 2,
            }
            return Response(res)

        if user:
            result = {
                'status': 1,
                'data': CustomuserSerializer(user, many=False, context={"request": request}).data,
                'token': token
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            res = {
                'status': 0,
                'msg': 'Can not authenticate with the given credentials or the account has been deactivated'
            }
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)

#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated, ])
# def login(request):
#     try:
#         user = Customuser.objects.username


@api_view(['GET'])
@permission_classes([AllowAny, ])
def me(request):
    try:
        user = request.user
        result = {
            'status': 1,
            'user': CustomuserSerializer(user, many=False, context={"request": request}).data
        }
        return Response(result, status=status.HTTP_200_OK)
    except KeyError:
        res = {
            'status': 0,
            'msg': 'Please set all reqiured fields'
        }
        return Response(res)

