# Generated by Django 2.2.10 on 2020-03-06 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blacklistApp', '0005_auto_20200306_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='abonent_added',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
