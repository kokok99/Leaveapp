# Generated by Django 4.1 on 2022-08-29 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cawangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cawangan', models.OneToOneField(choices=[('PASTI SEMBULAN', 'PASTI SEMBULAN'), ('PASTI ASY SYAKIRIN', 'PASTI ASY SYAKIRIN'), ('PASTI RAUDAH', 'PASTI RAUDAH'), ('PASTI PETAGAS', 'PASTI PETAGAS'), ('PASTI CERIAMAS', 'PASTI CERIAMAS'), ('PASTI PASIR PUTIH', 'PASTI PASIR PUTIH'), ('PASTI KETIAU', 'PASTI KETIAU')], on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
