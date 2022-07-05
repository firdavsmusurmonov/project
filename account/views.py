from django.shortcuts import render, redirect
from rest_framework import status, mixins, viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_jwt.settings import api_settings
from account.models import Customuser, Region
from account.serializer import CustomuserSerializer, RegionListSerializer
from rest_framework.decorators import api_view, permission_classes

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Customuser.objects.all()
    serializer_class = CustomuserSerializer
    # pagination_class = LargeResultsSetPagination
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['first_name']
    search_fields = ['first_name']


def homepage(request):
    return render(request, template_name="home.html", context={})


def register(request):
    user = Customuser.objects.filter(username=request.POST.get("username")).first()
    if user:
        return render(request, template_name="home.html", context={"error": "user exits"})
    if request.POST.get():
        user = Customuser.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            gender=request.POST.get('gender'),
            birth_date=request.POST.get('birth_date'),
            country_birth=request.POST.get('country_birth'),
            region_birth=request.POST.get('region_birth'),
            city_birth=request.POST.get('city_birth'),
            passport=request.POST.get('passport'),
            passport_date=request.POST.get('passport_date'),
            country=request.POST.get('country'),
            region=request.POST.get('region'),
            city=request.POST.get('city'),
            fulladress=request.POST.get('fulladress'),
            education=request.POST.get('education'),
            family=request.POST.get("family")

            )
        user.save()
    else:
        return render(request, template_name="base.html", context={"error":"Password error"})
    return redirect("/homepage")

    # if 'avatar' in request.data:
    #     user.avatar = request.data['avatar'],
    # return render(request, template_name="base.html")


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
        phone = request.data.get('phone')
        gender = request.data.get('gender')
        country_birth = int(request.data.get('country_birth'))
        region_birth = int(request.data.get('region_birth'))
        city_birth = int(request.data.get('city_birth'))
        passport = request.data.get('passport')
        passport_date = request.data.get('passport_date')
        country = int(request.data.get('country'))
        region = int(request.data.get('region'))
        city = int(request.data.get('city'))
        fulladress = request.data.get('fulladress')
        education = int(request.data.get('education'))
        family = int(request.data.get("family"))
        birth_date = request.data.get('birth_date')

        user = Customuser.objects.filter(username=first_name).first()
        if not user:
            if 'avatar' in request.data:
                user.avatar = request.data['avatar']
            user = Customuser.objects.create(
                username=first_name,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                birth_date=birth_date,
                country_birth_id=country_birth,
                region_birth_id=region_birth,
                city_birth_id=city_birth,
                passport=passport,
                passport_date=passport_date,
                country_id=country,
                region_id=region,
                city_id=city,
                fulladress=fulladress,
                phone=phone,
                education_id=education,
                family_id=family,
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
                'token': token,
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


# @api_view(['GET'])
# @permission_classes([AllowAny, ])
# def me(request):
#     try:
#         user = request.user
#         print(CustomuserSerializer(user, many=False, context={"request": request}).data)
#         result = {
#             'status': 1,
#             'user': CustomuserSerializer(user, many=False, context={"request": request}).data
#         }
#         return Response(result, status=status.HTTP_200_OK)
#     except KeyError:
#         res = {
#             'status': 0,
#             'msg': 'Please set all reqiured fields'
#         }
#         return Response(res)


class Me(viewsets.ModelViewSet, mixins.ListModelMixin):
    queryset = Customuser.objects.all()
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        user = request.user.pk
        print(request.user)
        user = Customuser.objects.filter(id=user)
        serializer = CustomuserSerializer(user, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def update_profil_img(request):
    user = request.user
    user.status = request.data.get('status')
    if 'avatar' in request.data:
        user.avatar = request.data['avatar']
        user.save()
    return Response(status=status.HTTP_200_OK, data={'status': 'ok'})
