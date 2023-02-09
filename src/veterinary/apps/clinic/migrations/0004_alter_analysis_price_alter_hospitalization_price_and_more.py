# Generated by Django 4.1.4 on 2022-12-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinic", "0003_alter_treatment_treatment_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analysis",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, verbose_name="Precio"
            ),
        ),
        migrations.AlterField(
            model_name="hospitalization",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, verbose_name="Precio"
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="total",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, verbose_name="Total"
            ),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=7, verbose_name="Precio"
            ),
        ),
    ]