# Generated by Django 4.1.2 on 2023-01-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_notes_options_rename_created_notes_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='create',
        ),
    ]
