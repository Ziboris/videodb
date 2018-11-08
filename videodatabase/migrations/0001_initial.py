# Generated by Django 2.1.3 on 2018-11-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVE_Case',
            fields=[
                ('case_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('jumpArg', models.IntegerField()),
                ('speedArg', models.IntegerField()),
                ('positionArg', models.IntegerField()),
                ('cramArg', models.IntegerField()),
                ('colorArg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CVE_Case_Tags',
            fields=[
                ('case_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('product_type', models.IntegerField()),
                ('busi_orientation', models.IntegerField()),
                ('product_style', models.IntegerField()),
                ('media', models.IntegerField()),
                ('year', models.IntegerField()),
                ('consumer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CVE_Shot',
            fields=[
                ('shot_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('case_id', models.IntegerField()),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('during', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('position', models.IntegerField()),
                ('craMotion', models.IntegerField()),
                ('color', models.IntegerField()),
                ('shotSize', models.IntegerField()),
            ],
        ),
    ]