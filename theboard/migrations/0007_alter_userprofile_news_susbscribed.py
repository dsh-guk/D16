# Generated by Django 4.0.1 on 2022-01-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theboard', '0006_remove_userprofile_id_userprofile_news_susbscribed_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='news_susbscribed',
            field=models.BooleanField(default=True, verbose_name='Newsletter subscription'),
        ),
    ]