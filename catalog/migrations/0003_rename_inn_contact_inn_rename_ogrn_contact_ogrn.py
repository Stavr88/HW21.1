# Generated by Django 4.2.15 on 2024-08-31 11:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="INN",
            new_name="inn",
        ),
        migrations.RenameField(
            model_name="contact",
            old_name="OGRN",
            new_name="ogrn",
        ),
    ]
