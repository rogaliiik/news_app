# Generated by Django 4.0 on 2022-01-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0013_remove_news_tags_tag_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='news',
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='app_news.Tag'),
        ),
    ]