# Generated by Django 2.2.1 on 2019-05-08 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20190508_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='color',
        ),
    ]
