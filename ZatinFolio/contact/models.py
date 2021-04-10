from django.db import models
from django.utils import timezone

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    subject = models.TextField(blank=False)
    message = models.TextField(blank=False)
    date_send = models.DateTimeField(default=timezone.now, editable=False)

    
