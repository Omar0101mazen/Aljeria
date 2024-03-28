from django.db import models

# Create your models here.


class Normal(models.Model):
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=50)
    mother_name = models.CharField( max_length=50)
    fathers_name = models.CharField( max_length=50)
    location = models.CharField(max_length=100)
    phone = models.IntegerField()
    commercial_registration_no = models.IntegerField()
    date_of_commercial = models.DateField()
    card_number_artisan =  models.IntegerField()
    date_of_artisan = models.DateField()
    written_request = models.FileField(upload_to='written_request/')
    property_contract = models.FileField(upload_to='property_contract/')
    site_plan = models.FileField(upload_to='site_plan/')
    block_plan = models.FileField(upload_to='block_plan/')
    technical_data_sheet = models.FileField(upload_to='technical_data_sheet/')
    report = models.FileField(upload_to='report/')