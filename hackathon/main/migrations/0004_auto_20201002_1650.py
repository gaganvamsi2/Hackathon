# Generated by Django 3.0.7 on 2020-10-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201002_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department_id',
        ),
        migrations.AddField(
            model_name='student',
            name='department_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='department_id',
        ),
        migrations.AddField(
            model_name='teacher',
            name='department_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
