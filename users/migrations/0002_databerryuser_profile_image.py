# Generated by Django 4.1.1 on 2022-11-08 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="databerryuser",
            name="profile_image",
            field=models.ImageField(default="", upload_to="users/"),
        ),
    ]
