from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer

from Pet_Shop.pets.models import Items, Users, Category, Orders, FavouriteItems, ItemsOrders


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


class OrdersItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsOrders
        fields = ['item_id', 'quantity']


class OrdersSerializer(serializers.ModelSerializer):
    items = OrdersItemSerializer(many=True, write_only=True)
    user_id = serializers.ReadOnlyField(source='user.id')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Orders.objects.create(**validated_data)
        for item_data in items_data:
            ItemsOrders.objects.create(order_id=order, **item_data)
        return order

    class Meta:
        model = Orders
        fields = '__all__'

