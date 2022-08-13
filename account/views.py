from django.shortcuts import render, redirect
from rest_framework import status, mixins, viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework_jwt.settings import api_settings
from account.models import Customuser
from account.serializer import CustomuserSerializer
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
    users = Customuser.objects.all()
    context = {
        "birth_date": ['1', '2', '3', '4', '5', '6', '7', '8'],
        "month_date": ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentyabr", "Oktyabr",
                       "Noyabr",
                       "Dekabr"]
    }
    return render(request, template_name="home.html", context=context)
    # return render(request, template_name="home.html", context={})


def register(request):
    # user = Customuser.objects.filter(username=request.POST.get("username")).first()
    # if user:
    #     return render(request, template_name="home.html", context={"error": "user exits"})
    if request.POST.get():
        user = Customuser.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            phone=request.POST.get('phone'),
            avatar=request.POST.get('avatar'),
            gender=request.POST.get('gender'),
            date=request.POST.get('date'),
            month=request.POST.get('month'),
            year=request.POST.get('year'),
            region_birth=request.POST.get('region_birth'),
            city_birth=request.POST.get('city_birth'),
            region=request.POST.get('region'),
            city=request.POST.get('city'),
            fulladress=request.POST.get('fulladress'),
            passport=request.POST.get('passport'),
            passport_date=request.POST.get('passport_date'),
            passport_month=request.POST.get('passport_month'),
            passport_year=request.POST.get("passport_year"),
            education=request.POST.get('education'),
            family=request.POST.get('family'),
            wife_first_name=request.POST.get('wife_first_name'),
            wife_last_name=request.POST.get('wife_last_name'),
            wife_gender=request.POST.get('wife_gender'),
            wife_date=request.POST.get('wife_date'),
            wife_month=request.POST.get('wife_month'),
            wife_year=request.POST.get('wife_year'),
            wife_region_birth=request.POST.get('wife_region_birth'),
            wife_city_birth=request.POST.get('wife_city_birth'),
            wife_avatar=request.POST.get('wife_avatar'),
            wife_education=request.POST.get('wife_education'),
            childs=request.POST.get('childs'),
        )
        user.save()
    else:
        context = {
            "birth_date": ['1', '2', '3', '4', '5', '6', '7', '8'],
        }
        return render(request, template_name="home.html", context=context)
    context = {
        "birth_date": ['1', '2', '3', '4', '5', '6', '7', '8'],
    }
    return render(request, template_name="base.html", context=context)


# def weatherpage(request):
#     print(request.user.is_authenticated)
#     if not request.user.is_authenticated:
#         return redirect("/loginPage")
#     context = {
#         "superuser": Superuser.objects.all(),
#         "image_1": ['https://img2.goodfon.com/original/960x544/e/2f/arka-arki-priroda-peyzazhi.jpg'],
#         "images": ['http://placehold.it/140x100', 'http://placehold.it/140x100', 'http://placehold.it/140x100',
#                    'http://placehold.it/140x100', 'http://placehold.it/140x100', 'http://placehold.it/140x100'],
#         "item": ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8'],
#         "lorem": [
#             'Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum officia non minima, eveniet, neque facere sapiente quam totam odio nam omnis praesentium deleniti quaerat optio unde ea, impedit a doloremin. Perspiciatis, nostrum deleniti qui corporis numquam id consequatur nisi eius reprehenderit at,molestiae accusamus sapiente quas neque ut deserunt autem perferendis quisquam commodi ducimus aliquam.Culpa, perferendis harum reprehenderit iste blanditiis similique sit tempore minus. Dolorem fuga sitet?']
#     }
#     return render(request, template_name="weather.html", context=context)

# if 'avatar' in request.data:
#     user.avatar = request.data['avatar'],
# return render(request, template_name="base.html")


# @api_view(['GET'])
# @permission_classes([AllowAny, ])
# def region(request):
#     region_id = request.GET.get("region_id")
#     if region_id:
#         region_id = Region.objects.filter(parent_id=region_id).all()
#     else:
#         region_id = Region.objects.filter(parent__isnull=True).all()
#
#     res = {
#         'status': 1,
#         'data': RegionListSerializer(region_id, many=True, context={"request": request}).data,
#     }
#     return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def registr(request):
    try:
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone = request.data.get('phone')
        avatar = request.File.get('avatar')
        gender = request.data.get('gender')
        date = request.data.get('date')
        month = request.data.get('month')
        year = request.data.get('year')
        region_birth = request.data.get('region_birth')
        city_birth = request.data.get('city_birth')
        region = request.data.get('region')
        city = request.data.get('city')
        fulladress = request.data.get("fulladress")
        passport = request.data.get('passport')
        passport_date = request.data.get("passport_date")
        passport_month = request.data.get("passport_month")
        passport_year = request.data.get("passport_year")
        education = request.data.get("education")
        family = request.data.get("family")
        wife_first_name = request.data.get("wife_first_name")
        wife_last_name = request.data.get("wife_last_name")
        wife_gender = request.data.get("wife_gender")
        wife_date = request.data.get("wife_date")
        wife_month = request.data.get("wife_month")
        wife_year = request.data.get("wife_year")
        wife_region_birth = request.data.get("wife_region_birth")
        wife_city_birth = request.data.get("wife_city_birth")
        wife_avatar = request.data.get("wife_avatar")
        wife_education = request.data.get("wife_education")
        childs = request.data.get("childs")

        user = Customuser.objects.filter(username=first_name).first()
        if not user:
            if 'avatar' in request.data:
                user.avatar = request.data['avatar']
            user = Customuser.objects.create(
                username=first_name,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                avatar=avatar,
                gender=gender,
                date=date,
                month=month,
                year=year,
                region_birth=region_birth,
                city_birth=city_birth,
                region=region,
                city=city,
                fulladress=fulladress,
                passport=passport,
                passport_date=passport_date,
                passport_month=passport_month,
                passport_year=passport_year,
                education=education,
                family=family,
                wife_first_name=wife_first_name,
                wife_last_name=wife_last_name,
                wife_gender=wife_gender,
                wife_date=wife_date,
                wife_month=wife_month,
                wife_year=wife_year,
                wife_region_birth=wife_region_birth,
                wife_city_birth=wife_city_birth,
                wife_avatar=wife_avatar,
                wife_education=wife_education,
                childs=childs,
                complete=1
            )
        elif user:
            res = {
                'msg': 'User exits',
                'status': 2,
            }
            return Response(res)

        if user:
            result = {
                'status': 'ok',
                'data': CustomuserSerializer(user, many=False, context={"request": request}).data
                # 'token': token,
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


@api_view(['GET'])
@permission_classes([AllowAny, ])
def me(request):
    try:
        user = request.user
        print(CustomuserSerializer(user, many=False, context={"request": request}).data)
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
@permission_classes([AllowAny, ])
def update_profil_img(request):
    user = request.user
    user.status = request.data.get('status')
    if 'avatar' in request.data:
        user.avatar = request.data['avatar']
        user.save()
    return Response(status=status.HTTP_200_OK, data={'status': 'ok'})
#
#
# def avatar(request):
#     # if not request.user.is_authenticated:
#     #     return redirect("/loginPage")
#     avatar = Customuser.objects.all()
#     context = {
#         "data": avatar,
#     }
#     return render(request, template_name="home.html", context=context)
