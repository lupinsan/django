# Generated by Django 4.2.2 on 2023-06-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app01", "0002_helporder_create_datetime_helporder_update_datetime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="helporder",
            name="update_datetime",
            field=models.DateTimeField(blank=True, null=True, verbose_name="完成时间"),
        ),
    ]
