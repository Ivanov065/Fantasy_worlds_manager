# Generated by Django 5.2.1 on 2025-05-20 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node_manager', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='creator',
            field=models.ForeignKey(default=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='node_owner', to=settings.AUTH_USER_MODEL), editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='node_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
