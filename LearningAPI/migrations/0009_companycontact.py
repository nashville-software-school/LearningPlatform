# Generated by Django 2.0.6 on 2018-06-18 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearningAPI', '0008_placement'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.Company')),
                ('contact_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='LearningAPI.Contact')),
            ],
        ),
    ]