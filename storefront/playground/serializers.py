from django.db.models import fields
from rest_framework import serializers
from .models import Item,MyModel,Login,asik

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ('category', 'subcategory', 'name', 'amount')


class MyModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyModel
		fields = ('name', 'age')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['name', 'password']


class asikSerializer(serializers.ModelSerializer):
	class Meta:
		model = asik
		fields = ('Temparature', 'HR_And_SPo2', 'EGG', 'Time')
