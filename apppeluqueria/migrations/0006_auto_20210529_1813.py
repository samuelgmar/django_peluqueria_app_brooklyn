# Generated by Django 3.1.7 on 2021-05-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apppeluqueria', '0005_galeria'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galeria',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='imagen',
            field=models.ImageField(blank=True, default='img_avatar.png', null=True, upload_to=''),
        ),
    ]