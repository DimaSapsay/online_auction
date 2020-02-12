from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


def image_directory_path(instance, filename):
    return f'gallery/user_{instance.user.id}/{filename}'


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to=image_directory_path, null=True, blank=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)

    def __str__(self):
        return self.name
