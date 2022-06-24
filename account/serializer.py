from rest_framework import serializers
from account.models import *


#
# class RegionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Region
#         fields = ["id", "name"]

class RegionListSerializer(serializers.ModelSerializer):
    childs = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField()

    class Meta:
        model = Region
        fields = ["id", "name", "childs"]

    def get_name(self, obj):
        request = self.context.get('request')
        data = request.GET if hasattr(request, 'GET') else {}
        language = data['lan'] if 'lan' in data else 'uz'
        return getattr(obj, 'name_' + language)

    def get_childs(self, instance):
        if hasattr(instance, "childs"):
            return RegionListSerializer(
                instance.childs, many=True,
                context={'request': self.context['request']}
            ).data
        else:
            return None


class CustomuserSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()


    class Meta:
        model = Customuser
        # fields = '__all__'
        fields = ['id', 'first_name', 'last_name', 'email', 'gender', 'country', 'region', 'city', 'phone',
                  'birth_date',
                  'passport']

    def get_country(self, obj):
        return RegionListSerializer(obj.region, many=False, context={'request': self.context['request']}).data

    def get_region(self, obj):
        return RegionListSerializer(obj.region, many=False, context={'request': self.context['request']}).data

    def get_city(self, obj):
        return RegionListSerializer(obj.city, many=False, context={'request': self.context['request']}).data
