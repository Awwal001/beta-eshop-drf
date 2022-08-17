from django.contrib.auth.models import User
from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=255)
    description = description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    vendor = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    