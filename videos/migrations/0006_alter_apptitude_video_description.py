# Generated by Django 4.0.2 on 2022-04-21 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_interview_corner_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apptitude_video',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
