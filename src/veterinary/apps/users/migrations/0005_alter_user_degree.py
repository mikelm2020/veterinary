# Generated by Django 4.1.4 on 2022-12-24 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_professional_license"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="degree",
            field=models.CharField(
                blank=True,
                choices=[("S", "Superior"), ("M", "Media"), ("B", "Básica")],
                max_length=1,
                null=True,
                verbose_name="Grado Escolar",
            ),
        ),
    ]
