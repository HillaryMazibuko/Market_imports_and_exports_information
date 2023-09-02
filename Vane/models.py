from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email_address = models.EmailField(max_length=255)
  date_joined = models.DateField(auto_now_add=True)
  date_of_birth = models.DateField()
  country = models.CharField(max_length=2550)