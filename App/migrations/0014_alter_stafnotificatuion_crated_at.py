# Generated by Django 5.0.6 on 2024-06-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_stafnotificatuion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stafnotificatuion',
            name='crated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]