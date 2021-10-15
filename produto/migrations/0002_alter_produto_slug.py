# Generated by Django 3.2.8 on 2021-10-14 21:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='nome', unique=True),
        ),
    ]
