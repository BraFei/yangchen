# Generated by Django 2.0 on 2018-05-19 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180518_1525'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='nongdu',
            new_name='concentration',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='shebeihao',
        ),
    ]
