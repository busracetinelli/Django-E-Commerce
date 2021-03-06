# Generated by Django 2.0.9 on 2019-04-08 20:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoecommerce_app', '0006_auto_20190408_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstar',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yıldız Veren Kişi'),
        ),
        migrations.AlterField(
            model_name='productstar',
            name='star',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Yıldız'),
        ),
    ]
