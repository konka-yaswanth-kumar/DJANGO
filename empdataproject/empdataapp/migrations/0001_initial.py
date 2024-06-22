# Generated by Django 5.0.6 on 2024-06-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email_id', models.EmailField(max_length=100)),
                ('Mobile_number', models.BigIntegerField()),
                ('Qualification', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=100)),
                ('Percentage', models.IntegerField()),
                ('Passed_out_year', models.IntegerField()),
                ('Skill_set', models.CharField(max_length=100)),
            ],
        ),
    ]
