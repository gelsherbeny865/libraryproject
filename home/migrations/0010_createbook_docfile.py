# Generated by Django 3.2.7 on 2021-10-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_bookinstance'),
    ]

    operations = [
        migrations.AddField(
            model_name='createbook',
            name='docfile',
            field=models.FileField(default=1, upload_to='documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
