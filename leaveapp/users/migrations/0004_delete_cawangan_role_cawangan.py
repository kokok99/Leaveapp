# Generated by Django 4.1 on 2022-08-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_cawangan_cawangan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='cawangan',
        ),
        migrations.AddField(
            model_name='role',
            name='cawangan',
            field=models.CharField(choices=[('Choose cawangan', 'Choose cawangan'), ('PASTI SEMBULAN', 'PASTI SEMBULAN'), ('PASTI ASY SYAKIRIN', 'PASTI ASY SYAKIRIN'), ('PASTI RAUDAH', 'PASTI RAUDAH'), ('PASTI PETAGAS', 'PASTI PETAGAS'), ('PASTI CERIAMAS', 'PASTI CERIAMAS'), ('PASTI PASIR PUTIH', 'PASTI PASIR PUTIH'), ('PASTI KETIAU', 'PASTI KETIAU')], default='Choose cawangan', max_length=100),
        ),
    ]
