# Generated by Django 4.1.2 on 2022-11-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_Offer', '0004_all_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_course',
            name='Course_Title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='all_course',
            name='Credits',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]