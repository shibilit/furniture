# Generated by Django 4.1.7 on 2023-04-04 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
        ('common', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
