# Generated by Django 3.1.7 on 2021-03-28 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=1023)),
                ('text', models.CharField(max_length=8191)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=1023)),
            ],
        ),
    ]