from rest_framework import serializers
from account.models import *


#
# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = ["id", "name"]
#
#
# class FamilySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = ["id", "name"]
#
#
# class RegionListSerializer(serializers.ModelSerializer):
#     childs = serializers.SerializerMethodField(read_only=True)
#     name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Region
#         fields = ["id", "name", "childs"]
#
#     def get_childs(self, instance):
#         if hasattr(instance, "childs"):
#             return RegionListSerializer(instance.childs, many=True, context={'request': self.context['request']}).data
#         else:
#             return None
#
#     def get_name(self, obj):
#         request = self.context.get('request')
#         data = request.GET if hasattr(request, 'GET') else {}
#         language = data['lan'] if 'lan' in data else 'uz'
#         return getattr(obj, 'name_' + language)


class CustomuserSerializer(serializers.ModelSerializer):
    # country = serializers.SerializerMethodField()
    # region = serializers.SerializerMethodField()
    # city = serializers.SerializerMethodField()
    # country_birth = serializers.SerializerMethodField()
    # region_birth = serializers.SerializerMethodField()
    # city_birth = serializers.SerializerMethodField()
    # education = serializers.SerializerMethodField()
    # family = serializers.SerializerMethodField()

    class Meta:
        model = Customuser
        # fields = '__all__'
        fields = ['id', 'first_name', 'last_name', 'gender', 'date', 'month', 'year', 'passport', 'passport_date',
                  'passport_month', 'passport_year', 'region_birth', 'avatar',
                  'city_birth', 'fulladress', 'phone', 'education',
                  'family', 'wife_first_name', 'wife_last_name', 'wife_gender', 'wife_date', 'wife_month', 'wife_year',
                  'wife_region_birth', 'wife_city_birth', 'wife_avatar', 'wife_education', 'childs']

    # def get_serializer(self, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super(cblk, self).get_serializer(*args, **kwargs)
    #
    # def get_country(self, obj):
    #     return RegionListSerializer(obj.country, many=False, context={'request': self.context['request']}).data

    # def get_region(self, obj):
    #     return RegionListSerializer(obj.region, many=False, context={'request': self.context['request']}).data
    #
    # def get_city(self, obj):
    #     return RegionListSerializer(obj.city, many=False, context={'request': self.context['request']}).data
    #
    # def get_country_birth(self, obj):
    #     return RegionListSerializer(obj.country_birth, many=False, context={'request': self.context['request']}).data

    # def get_region_birth(self, obj):
    #     return RegionListSerializer(obj.region_birth, many=False, context={'request': self.context['request']}).data
    #
    # def get_city_birth(self, obj):
    #     return RegionListSerializer(obj.city_birth, many=False, context={'request': self.context['request']}).data
    #
    # def get_education(self, obj):
    #     return EducationSerializer(obj.education, many=False, context={'request': self.context['request']}).data
    #
    # def get_family(self, obj):
    #     return FamilySerializer(obj.family, many=False, context={'request': self.context['request']}).data
