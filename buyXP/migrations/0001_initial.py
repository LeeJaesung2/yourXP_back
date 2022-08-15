# Generated by Django 3.2 on 2022-08-15 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyXP_tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag1', models.CharField(blank=True, max_length=100, null=True)),
                ('tag2', models.CharField(blank=True, max_length=100, null=True)),
                ('tag3', models.CharField(blank=True, max_length=100, null=True)),
                ('tag4', models.CharField(blank=True, max_length=100, null=True)),
                ('tag5', models.CharField(blank=True, max_length=100, null=True)),
                ('tag6', models.CharField(blank=True, max_length=100, null=True)),
                ('tag7', models.CharField(blank=True, max_length=100, null=True)),
                ('tag8', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BuyXP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('deadline', models.DateTimeField()),
                ('price', models.IntegerField(blank=True, null=True)),
                ('hits', models.IntegerField(default=0)),
                ('BuyXP_tag', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='buyXP.buyxp_tag')),
            ],
        ),
    ]
