# Generated by Django 4.1.4 on 2022-12-20 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_professional_license"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="professional_license",
            field=models.CharField(
                default="Ninguna", max_length=30, verbose_name="Cédula Profesional"
            ),
        ),
    ]
