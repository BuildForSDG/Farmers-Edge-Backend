# Generated by Django 3.0.6 on 2020-06-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200601_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Location',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]