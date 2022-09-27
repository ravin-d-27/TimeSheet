from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Times(models.Model):
    pub_date = models.DateTimeField()
    description = models.TextField()
    approved = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def limit(self):
        return self.body[0:51]
