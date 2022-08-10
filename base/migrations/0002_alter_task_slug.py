# Generated by Django 4.1 on 2022-08-06 21:21

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, null=True, populate_from="name"
            ),
        ),
    ]
