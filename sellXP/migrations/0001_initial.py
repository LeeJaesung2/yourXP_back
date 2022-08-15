# Generated by Django 4.1 on 2022-08-15 04:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sellXP.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sell_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=sellXP.models.image_upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('grad', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='SellXP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('hits', models.PositiveIntegerField(default=0)),
                ('recommend', models.PositiveIntegerField(default=0)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SellXP_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag1', models.CharField(max_length=100, null=True)),
                ('tag2', models.CharField(max_length=100, null=True)),
                ('tag3', models.CharField(max_length=100, null=True)),
                ('tag4', models.CharField(max_length=100, null=True)),
                ('tag5', models.CharField(max_length=100, null=True)),
                ('tag6', models.CharField(max_length=100, null=True)),
                ('tag7', models.CharField(max_length=100, null=True)),
                ('tag8', models.CharField(max_length=100, null=True)),
                ('tag9', models.CharField(max_length=100, null=True)),
                ('tag10', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
