# Generated by Django 2.2.2 on 2019-07-01 05:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190630_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favourite',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
