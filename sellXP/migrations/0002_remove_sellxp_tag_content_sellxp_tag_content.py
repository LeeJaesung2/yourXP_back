# Generated by Django 4.0.5 on 2022-08-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellXP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellxp',
            name='tag_content',
        ),
        migrations.AddField(
            model_name='sellxp',
            name='tag_content',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sellXP.sellxp_tag'),
        ),
    ]
