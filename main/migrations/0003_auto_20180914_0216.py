# Generated by Django 2.1.1 on 2018-09-13 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userinfor_usiusi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfor',
            name='profpic',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]