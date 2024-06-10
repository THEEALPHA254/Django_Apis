from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
