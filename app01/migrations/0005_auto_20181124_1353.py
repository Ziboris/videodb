# Generated by Django 2.1.3 on 2018-11-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_remove_cve_case_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cve_case',
            name='case_id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
