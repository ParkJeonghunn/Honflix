# Generated by Django 4.0.1 on 2022-02-04 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likecomment',
            name='nickname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contentmodel',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='content.category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.contentmodel'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
