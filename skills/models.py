from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='skills/icons/', blank=True, null=True)

    def __str__(self):
        return self.name
