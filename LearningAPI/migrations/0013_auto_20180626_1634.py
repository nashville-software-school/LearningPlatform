# Generated by Django 2.0.6 on 2018-06-26 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0012_auto_20180626_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placement',
            old_name='company_id',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='placement',
            old_name='job_type_id',
            new_name='job_type',
        ),
        migrations.RenameField(
            model_name='placement',
            old_name='nss_user_id',
            new_name='nss_user',
        ),
    ]
