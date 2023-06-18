# Generated by Django 4.1.1 on 2022-11-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course_Offer', '0002_course_rename_role_batch_delete_employee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='first_name',
            new_name='Course_Code',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='last_name',
            new_name='Course_Title',
        ),
        migrations.RemoveField(
            model_name='course',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='course',
            name='hire_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='course',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='department',
            name='location',
        ),
        migrations.AddField(
            model_name='course',
            name='Credits',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
