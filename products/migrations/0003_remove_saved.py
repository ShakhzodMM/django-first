from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('users', '0003_saved'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.DeleteModel(
                    name='Saved',
                ),
            ],
        ),
    ]
