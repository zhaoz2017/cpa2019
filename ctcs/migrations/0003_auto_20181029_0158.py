# Generated by Django 2.1.2 on 2018-10-29 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctcs', '0002_auto_20181028_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_number', models.CharField(max_length=8)),
            ],
        ),
        migrations.RenameField(
            model_name='ctcs',
            old_name='Registration_semeter',
            new_name='Registration_semester',
        ),
    ]