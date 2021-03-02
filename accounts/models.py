from django.db import models
from django.contrib.auth.models import User



class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to = "photos/Y%/%m/%d/", null=True)
    lastname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    biography = models.TextField()



    def __str__(self):
        return f"{self.first_name} - {self.lastname}"
