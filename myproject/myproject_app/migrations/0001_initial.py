# Generated by Django 4.2.7 on 2023-11-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.CharField(max_length=7)),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]