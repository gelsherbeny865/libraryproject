# Generated by Django 3.2.7 on 2021-10-13 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_bookinstance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookInstance',
        ),
    ]