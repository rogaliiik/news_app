# Generated by Django 4.0 on 2022-01-13 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_alter_tag_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='news',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='app_news.News'),
        ),
    ]