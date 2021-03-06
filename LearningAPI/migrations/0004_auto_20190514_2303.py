# Generated by Django 2.2.1 on 2019-05-14 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0003_auto_20190513_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cohort',
            options={'ordering': ['start_date']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name']},
        ),
        migrations.CreateModel(
            name='InstructorStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.Instructor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.Student')),
            ],
        ),
        migrations.AddField(
            model_name='instructor',
            name='students',
            field=models.ManyToManyField(through='LearningAPI.InstructorStudent', to='LearningAPI.Student'),
        ),
    ]
