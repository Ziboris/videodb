# Generated by Django 2.1.3 on 2018-11-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20181124_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cve_case',
            name='case_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='video_id'),
        ),
        migrations.AlterField(
            model_name='cve_shot',
            name='shot_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='shot_id'),
        ),
    ]
