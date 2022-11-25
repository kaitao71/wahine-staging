# Generated by Django 4.1.2 on 2022-11-04 05:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]