# Generated by Django 3.2.8 on 2023-04-21 10:43

import django.db.models.deletion
from django.db import migrations, models

import ob_dj_store.utils.model


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0075_auto_20230419_0259"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="busy_mode",
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name="AvailabilityHours",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "weekday",
                    models.IntegerField(
                        choices=[
                            (1, "Monday"),
                            (2, "Tuesday"),
                            (3, "Wednesday"),
                            (4, "Thursday"),
                            (5, "Friday"),
                            (6, "Saturday"),
                            (7, "Sunday"),
                        ]
                    ),
                ),
                ("from_hour", models.TimeField()),
                ("to_hour", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="availability_hours",
                        to="stores.category",
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="availability_hours",
                        to="stores.store",
                    ),
                ),
            ],
            options={
                "ordering": ("weekday", "from_hour"),
                "unique_together": {("weekday", "store", "category")},
            },
            bases=(ob_dj_store.utils.model.DjangoModelCleanMixin, models.Model),
        ),
    ]
