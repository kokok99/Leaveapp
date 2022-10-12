from errno import EFAULT
from django.db import models
from leaveapp import settings
from django_resized import ResizedImageField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Staff(models.Model) :
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

    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    cawangan = models.CharField(max_length=100, choices=CAWANGAN_CHOICES, default='Choose cawangan')
    image =  ResizedImageField(size=[300, 300],default='default.jpg', upload_to='profile-pics', blank=True, null=True)
    tahunan = models.IntegerField(default=10)
    sakit = models.IntegerField(default=15)
    bersalin = models.IntegerField(default=60)
    haji = models.IntegerField(default=46)
    umrah = models.IntegerField(default=17)

    def __str__(self):
        return self.fullname


class Application(models.Model) :
    LEAVE_CHOICES = (
        ('Pilih Cuti', 'Pilih Cuti'),
        ('Cuti Tahunan', 'Cuti Tahunan'),
        ('Cuti Sakit', 'Cuti Sakit'),
        ('Cuti Kecemasan', 'Cuti kecemasan'),
        ('Cuti Bersalin', 'Cuti Bersalin'),
        ('Cuti Haji', 'Cuti Haji'),
        ('Cuti Umrah', 'Cuti Umrah'),
    )
    STATUS_CHOICES = (
        ('Approve', 'Approve'),
        ('Reject', 'Reject')
    )
    pemohon = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    leave = models.CharField(max_length=100, choices=LEAVE_CHOICES, default='Choose Leave')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    days = models.IntegerField(null=True)
    details = models.CharField(max_length=300, null=True)
    attachment = models.FileField(upload_to='doc', null=True, blank=True)

    class Meta:
        ordering = ('-date_created',)

    
