# Generated by Django 4.1.7 on 2023-03-30 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appadmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_username', models.CharField(max_length=100)),
                ('A_pssword', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'app_admin',
            },
        ),
    ]
