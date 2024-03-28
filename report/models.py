from django.db import models
from django.utils.text import slugify
# Create your models here.
class Reports(models.Model):
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    classification_of_the_establishment = models.CharField(max_length=300)
    decree_number = models.IntegerField()
    date_of_decree_issuance = models.DateField()
    public_inquiry_number = models.IntegerField()
    date_of_public_inquiry_issuance = models.DateField()
    duration = models.CharField(max_length=100)
    start_date_of_the_duration = models.DateField()
    end_date_of_the_duration = models.DateField()
    request_of_mr = models.CharField(max_length=75)
    exploitation_of_the_classified_establishment = models.CharField(max_length=75)
    located_in = models.CharField(max_length=75)
    designation = models.CharField(max_length=75)
    photo = models.ImageField(upload_to='photo/',null = True, blank=True)
    slug = models.SlugField(blank=True,null=True)
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.id)
        super(Reports,self).save(*args, **kwargs)
        
class Comment(models.Model):
    name = models.CharField(max_length=50, blank=True,null = True)
    email = models.EmailField(max_length=254, blank=True,null = True)
    titl = models.ForeignKey(Reports, related_name=("aplly_job"), on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null = True)