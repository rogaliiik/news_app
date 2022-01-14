# Generated by Django 4.0 on 2022-01-14 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app_news', '0015_alter_commentary_options_alter_news_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
