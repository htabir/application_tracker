# Generated by Django 4.1.5 on 2023-01-08 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('application', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='users',
                                    to='application.group', verbose_name='Group'),
            preserve_default=False,
        ),
    ]
