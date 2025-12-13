# webapp/migrations/0002_add_types_field.py
from django.db import migrations, models


def add_types_field(apps, schema_editor):
    Issue = apps.get_model('webapp', 'Issue')
    for issue in Issue.objects.all():
        issue.types.set([issue.type])


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='types',
            field=models.ManyToManyField(to='webapp.Type', blank=True),
        ),
        migrations.RunPython(add_types_field),
    ]

