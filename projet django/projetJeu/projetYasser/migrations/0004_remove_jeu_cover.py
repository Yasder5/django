# Generated by Django 5.0.6 on 2024-05-12 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projetYasser', '0003_jeu_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jeu',
            name='cover',
        ),
    ]
