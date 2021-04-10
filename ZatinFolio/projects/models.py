from django.db import models
from versatileimagefield.fields import PPOIField, VersatileImageField
# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(max_length=128, blank=False, null=False)
    company = models.CharField(max_length=128, blank=False, null=True)
    dev_team= models.CharField(max_length=128, blank=False, null=True)
    duration = models.CharField(max_length=128, blank=False, null=True)
    url = models.URLField(max_length=258,blank=False,null=True)
    description = models.TextField()
    status = models.TextField(max_length=28,blank=False,null=True)
    image = models.ImageField(upload_to='project_image/', default='project_image/NO_IMAGE.jpg',
                              height_field='height_field', width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
