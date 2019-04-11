# Generated by Django 2.1.2 on 2019-04-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20181125_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_prog_plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=30)),
                ('ureq_num', models.IntegerField()),
                ('met_flag', models.IntegerField()),
                ('usub', models.CharField(max_length=30)),
                ('unum', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AddField(
            model_name='profile',
            name='progplan',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='starting_semester',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='starting_year',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]