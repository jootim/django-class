# Generated by Django 5.0.7 on 2024-08-19 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_toppic_room_user_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
