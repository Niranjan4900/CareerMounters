# Generated by Django 4.0.2 on 2022-04-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil_Course',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('courseLink', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Electrical_Course',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('courseLink', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entc_Course',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('courseLink', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mechanical_Course',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('Free', 'Free'), ('Paid', 'Paid')], default='Free', max_length=10)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('courseLink', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='cs_it_course',
            name='courseLink',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
