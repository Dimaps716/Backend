# Generated by Django 3.1.4 on 2020-12-18 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201218_1450'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='week1',
            new_name='week',
        ),
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['id'], 'verbose_name': 'week1', 'verbose_name_plural': 'weeks1'},
        ),
    ]