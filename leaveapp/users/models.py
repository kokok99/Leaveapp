from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField



# Create your models here.
class Role(AbstractUser) :
    CAWANGAN_CHOICES = (
        ('Choose cawangan', 'Choose cawangan'),
        ('PASTI SEMBULAN', 'PASTI SEMBULAN'),
        ('PASTI ASY SYAKIRIN', 'PASTI ASY SYAKIRIN'),
        ('PASTI RAUDAH', 'PASTI RAUDAH'),
        ('PASTI PETAGAS', 'PASTI PETAGAS'),
        ('PASTI CERIAMAS', 'PASTI CERIAMAS'),
        ('PASTI PASIR PUTIH', 'PASTI PASIR PUTIH'),
        ('PASTI KETIAU', 'PASTI KETIAU'),
    )
    is_admin = models.BooleanField(default=False)
    cawangan = models.CharField(max_length=100, choices=CAWANGAN_CHOICES, default='Choose cawangan')
    phone = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    image =  ResizedImageField(size=[300, 300],default='default.jpg', upload_to='profile-pics', blank=True, null=True)


    
       

