# Generated by Django 4.2.3 on 2023-10-28 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_order_delivery_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dish',
            options={'verbose_name': 'Dish', 'verbose_name_plural': 'Dishes'},
        ),
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='restaurant.restaurant'),
            preserve_default=False,
        ),
    ]