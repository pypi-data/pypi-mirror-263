# Generated by Django 3.2.8 on 2024-01-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0103_alter_paymentmethod_payment_provider"),
    ]

    operations = [
        migrations.AddField(
            model_name="wallettransaction",
            name="is_redeemed",
            field=models.BooleanField(default=False),
        ),
    ]
