# Generated by Django 2.0.6 on 2018-06-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0006_technology'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
    ]
