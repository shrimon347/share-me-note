# Generated by Django 4.1.2 on 2023-01-26 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_notes_options_notes_created_alter_contact_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={},
        ),
        migrations.RemoveField(
            model_name='notes',
            name='created',
        ),
    ]
