# Generated by Django 4.0.6 on 2022-08-18 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellXP', '0003_alter_sellxp_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellxp',
            name='like',
        ),
    ]
