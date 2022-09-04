# Generated by Django 3.2.12 on 2022-05-26 14:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
