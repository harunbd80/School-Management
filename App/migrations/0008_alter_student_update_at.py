# Generated by Django 5.0.6 on 2024-06-07 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
