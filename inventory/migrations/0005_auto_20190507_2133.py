from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20190507_0424'),
    ]

    operations = [
        TrigramExtension(),
    ]
