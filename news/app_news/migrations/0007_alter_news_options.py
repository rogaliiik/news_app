# Generated by Django 4.0 on 2022-01-10 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_alter_news_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_at'], 'permissions': (['can_publish', 'может публиковать'],)},
        ),
    ]
