# Generated by Django 4.0.6 on 2022-08-04 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('hash_tag', models.CharField(max_length=10)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
