# Generated by Django 2.1.1 on 2018-09-15 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180914_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='profpic',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
