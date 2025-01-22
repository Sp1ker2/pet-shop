from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer

from Pet_Shop.pets.models import Items, Users, Category, Orders, FavouriteItems


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Users.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    class Meta:
        model = Users
        fields = ['id', 'email', 'created_at', 'password']


class FavouriteItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouriteItems
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Orders
        fields = '__all__'

