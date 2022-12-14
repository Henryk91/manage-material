# Generated by Django 3.1.14 on 2022-07-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('waste', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deliveryitem',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery', to='facility.facility'),
        ),
        migrations.AddField(
            model_name='deliveryitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery_items', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deliveryitem',
            name='waste_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='delivery_waste_category', to='waste.wastecategory'),
        ),
    ]
