# Generated by Django 3.2 on 2022-08-18 11:13

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
            name='like',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sellxp',
            name='tag_content',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sellXP.sellxp_tag'),
        ),
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
        migrations.AddField(
            model_name='sell_review',
            name='user',
            field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sell_image',
            name='sellXP_id',
            field=models.ForeignKey(db_column='image_sellXP_id', on_delete=django.db.models.deletion.CASCADE, related_name='image', to='sellXP.sellxp'),
        ),
    ]
