# Generated by Django 2.2.1 on 2019-05-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CohortType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=55)),
            ],
        ),
    ]
