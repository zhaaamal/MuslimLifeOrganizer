# Generated by Django 4.2.6 on 2023-10-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_usersettings_delete_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSettings',
        ),
    ]