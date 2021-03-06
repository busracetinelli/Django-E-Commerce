# Generated by Django 2.1.8 on 2019-04-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0011_auto_20190412_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='link_facebook',
        ),
        migrations.RemoveField(
            model_name='company',
            name='link_instagram',
        ),
        migrations.RemoveField(
            model_name='company',
            name='link_twitter',
        ),
        migrations.RemoveField(
            model_name='company',
            name='link_web',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_verified',
        ),
        migrations.AddField(
            model_name='user',
            name='link_facebook',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Facebook Linki'),
        ),
        migrations.AddField(
            model_name='user',
            name='link_instagram',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Instagram Linki'),
        ),
        migrations.AddField(
            model_name='user',
            name='link_twitter',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Twitter Linki'),
        ),
        migrations.AddField(
            model_name='user',
            name='link_web',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Website Linki'),
        ),
    ]
