# Generated by Django 3.2.7 on 2021-09-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_experimentinstance_assignemnts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mturk_worker_id',
            field=models.CharField(blank=True, max_length=127, primary_key=True, serialize=False),
        ),
    ]