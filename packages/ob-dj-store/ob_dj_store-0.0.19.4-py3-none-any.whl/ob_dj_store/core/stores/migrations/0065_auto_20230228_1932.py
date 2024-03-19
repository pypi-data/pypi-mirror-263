# Generated by Django 3.2.8 on 2023-02-28 16:32

from django.db import migrations, models

import ob_dj_store.utils.helpers


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0064_auto_20230228_1814"),
    ]

    operations = [
        migrations.AddField(
            model_name="wallet",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=ob_dj_store.utils.helpers.wallet_media_upload_to,
            ),
        ),
        migrations.AddField(
            model_name="wallet",
            name="image_thumbnail_medium",
            field=models.ImageField(blank=True, null=True, upload_to="wallets/"),
        ),
        migrations.AddField(
            model_name="wallet",
            name="name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
