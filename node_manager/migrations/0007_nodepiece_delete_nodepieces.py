# Generated by Django 5.2.1 on 2025-05-28 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node_manager', '0006_nodes_root_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='NodePiece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece_name', models.CharField(max_length=200)),
                ('is_secret', models.BooleanField(default=True)),
                ('body', models.CharField()),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='node_manager.nodes')),
            ],
        ),
        migrations.DeleteModel(
            name='NodePieces',
        ),
    ]
