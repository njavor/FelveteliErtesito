# Generated by Django 4.0.3 on 2022-03-27 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('felvetel', '0009_tager_jelentkezo_tagozat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jelentkezo',
            name='tagozat',
        ),
        migrations.DeleteModel(
            name='TagEr',
        ),
    ]
