# Generated by Django 4.1.4 on 2022-12-27 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DicoverDesease",
            new_name="DicoverDisease",
        ),
    ]
