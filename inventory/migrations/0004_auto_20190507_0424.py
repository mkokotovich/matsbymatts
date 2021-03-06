# Generated by Django 2.2.1 on 2019-05-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddIndex(
            model_name='item',
            index=models.Index(fields=['description'], name='inventory_i_descrip_072d9d_idx'),
        ),
    ]
