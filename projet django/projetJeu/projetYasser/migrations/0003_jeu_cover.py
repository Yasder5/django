# Generated by Django 5.0.6 on 2024-05-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetYasser', '0002_rename_livre_jeu'),
    ]

    operations = [
        migrations.AddField(
            model_name='jeu',
            name='cover',
            field=models.ImageField(default=1, upload_to='uploads/% Y/% m/% d/'),
            preserve_default=False,
        ),
    ]
