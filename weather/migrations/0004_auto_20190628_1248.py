# Generated by Django 2.2.2 on 2019-06-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20190628_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(help_text='City Name', max_length=25),
        ),
        migrations.AlterField(
            model_name='city',
            name='temp',
            field=models.CharField(help_text='Temperature', max_length=25),
        ),
    ]
