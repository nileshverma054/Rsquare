from django.db import models

class users(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        db_table="users"