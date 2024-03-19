# Generated by Django 3.2.8 on 2023-03-09 19:51

from django.db import migrations, models

import ob_dj_store.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0067_auto_20230309_2014"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="optional image field",
                null=True,
                upload_to=ob_dj_store.utils.helpers.product_variant_media_upload_to,
            ),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="image_thumbnail_medium",
            field=models.ImageField(
                blank=True, null=True, upload_to="product_variant_media/"
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="extra_infos",
            field=models.JSONField(
                blank=True,
                help_text="\n                gift_details :  digital_product,price,email,phone_number,name\n                gift_card : the id of the gift_card\n\n            ",
                null=True,
            ),
        ),
    ]
