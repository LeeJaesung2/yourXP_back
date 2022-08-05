# Generated by Django 4.0.6 on 2022-08-05 01:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sellXP', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sellxp',
            name='user',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sell_review',
            name='sellXP_id',
            field=models.ForeignKey(db_column='sellXP_id', on_delete=django.db.models.deletion.CASCADE, related_name='sellXP', to='sellXP.sellxp'),
        ),
    ]