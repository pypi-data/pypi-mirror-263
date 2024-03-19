# Generated by Django 3.2.8 on 2022-12-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0053_inventory_plu"),
    ]

    operations = [
        migrations.AddField(
            model_name="attributechoice",
            name="external_id",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="attributechoice",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="category",
            name="external_id",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="category",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="product",
            name="external_id",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="product",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productattribute",
            name="external_id",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productattribute",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="external_id",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="inventory",
            name="plu",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
