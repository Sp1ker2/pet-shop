from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics
from .models import Items, Users, Orders, FavouriteItems
from .serializers import ItemsSerializer, UsersSerializer, FavouriteItemsSerializer, OrdersSerializer


class ItemsList(generics.ListCreateAPIView):

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class ItemDetail(generics.RetrieveAPIView):

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user.id)
