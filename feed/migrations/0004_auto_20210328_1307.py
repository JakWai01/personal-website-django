# Generated by Django 3.1.7 on 2021-03-28 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210328_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activity',
            new_name='Content',
        ),
    ]