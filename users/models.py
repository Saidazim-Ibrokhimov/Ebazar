from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomeUser(AbstractUser):
    phone_number = models.CharField(max_length=17)
    tg_username = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='users/avatars/', default='users/avatars/default_profile_pic.jpg')

    def __str__(self):
        return str(self.username)


class Saved(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Saved {self.product.title} {self.user.username}"
