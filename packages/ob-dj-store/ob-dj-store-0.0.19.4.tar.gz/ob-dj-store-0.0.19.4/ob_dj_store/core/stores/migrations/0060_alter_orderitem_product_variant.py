# Generated by Django 3.2.8 on 2023-02-22 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0059_auto_20230217_2006"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="product_variant",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="order_items",
                to="stores.productvariant",
            ),
        ),
    ]
