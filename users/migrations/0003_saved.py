from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
        ('users', '0002_alter_customuser_avatar'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Saved',
                    fields=[
                        ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('body', models.CharField(max_length=150)),
                        ('date_created', models.DateTimeField(auto_now_add=True)),
                        ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
                        ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                    ],
                    options={
                        'db_table': 'products_saved',
                    },
                ),
            ],
        ),
    ]
