# Generated by Django 2.0.6 on 2018-06-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0008_placement'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contacts',
            field=models.ManyToManyField(to='LearningAPI.Contact'),
        ),
    ]
