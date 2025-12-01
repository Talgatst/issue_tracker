from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20251201_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='type',
        ),
    ]

