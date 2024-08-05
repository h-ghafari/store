# Generated by Django 5.0.7 on 2024-08-05 08:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_created_at_customuser_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('Area_code', models.IntegerField()),
                ('address', models.TextField(max_length=150)),
                ('house_number', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
