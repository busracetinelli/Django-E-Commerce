# Generated by Django 2.1.8 on 2019-04-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0012_auto_20190419_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='link_facebook',
            field=models.CharField(blank=True, default='#', max_length=250, null=True, verbose_name='Facebook Linki'),
        ),
        migrations.AlterField(
            model_name='user',
            name='link_instagram',
            field=models.CharField(blank=True, default='#', max_length=250, null=True, verbose_name='Instagram Linki'),
        ),
        migrations.AlterField(
            model_name='user',
            name='link_twitter',
            field=models.CharField(blank=True, default='#', max_length=250, null=True, verbose_name='Twitter Linki'),
        ),
        migrations.AlterField(
            model_name='user',
            name='link_web',
            field=models.CharField(blank=True, default='#', max_length=250, null=True, verbose_name='Website Linki'),
        ),
    ]
