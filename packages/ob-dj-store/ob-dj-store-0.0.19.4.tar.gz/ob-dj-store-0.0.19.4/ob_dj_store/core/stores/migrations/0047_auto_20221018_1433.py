# Generated by Django 3.1.14 on 2022-10-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0046_auto_20221014_1720"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="attributechoice",
            options={
                "ordering": ["order_value", "created_at"],
                "verbose_name": "Attribute Choice",
                "verbose_name_plural": "Attribute Choices",
            },
        ),
        migrations.AlterModelOptions(
            name="productattribute",
            options={
                "ordering": ["order_value", "created_at"],
                "verbose_name": "Product Attribute",
                "verbose_name_plural": "Product Attributes",
            },
        ),
        migrations.AddField(
            model_name="attributechoice",
            name="order_value",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="ordering"),
        ),
        migrations.AddField(
            model_name="productattribute",
            name="order_value",
            field=models.PositiveSmallIntegerField(default=1, verbose_name="ordering"),
        ),
    ]
