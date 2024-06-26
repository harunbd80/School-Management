# Generated by Django 5.0.6 on 2024-06-07 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_course_session_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=50)),
                ('dateOfBrith', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField()),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.course')),
                ('session_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.session_year')),
            ],
        ),
    ]
