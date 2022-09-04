# Generated by Django 3.2.12 on 2022-05-26 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(blank=True, null=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
