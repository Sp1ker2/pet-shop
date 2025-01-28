from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title


class Items(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    logo = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Orders(models.Model):
    status = models.CharField(max_length=100, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey("pets.Users", on_delete=models.DO_NOTHING)


class FavouriteItems(models.Model):
    user_id = models.ForeignKey('pets.Users', on_delete=models.DO_NOTHING)
    item_id = models.ForeignKey('pets.Items', on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('user_id', 'item_id')

class ItemsOrders(models.Model):
    item_id = models.ForeignKey('pets.Items', on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey('pets.Orders', on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
