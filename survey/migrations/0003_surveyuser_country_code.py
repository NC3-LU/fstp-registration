# Generated by Django 2.2.7 on 2019-11-11 08:45
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0002_surveyuserfeedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyuser",
            name="country_code",
            field=models.CharField(default="LU", max_length=4),
        ),
    ]
