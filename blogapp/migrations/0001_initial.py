# Generated by Django 5.0.3 on 2024-03-20 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.category')),
            ],
        ),
    ]
