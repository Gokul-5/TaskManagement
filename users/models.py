from django.db import models

# first model
from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

