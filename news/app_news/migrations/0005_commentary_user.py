# Generated by Django 4.0 on 2022-01-02 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app_news', '0004_alter_commentary_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]