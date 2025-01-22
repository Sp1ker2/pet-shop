from rest_framework import serializers
from Pet_Shop.pets.models import Items, Users, Category, Orders, FavouriteItems


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `Items` instance, given the validated data.
        """
        return Items.objects.create(**validated_data)



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'email', 'created_at']


class FavouriteItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavouriteItems
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):

    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Orders
        fields = '__all__'