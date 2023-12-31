# Generated by Django 4.2.3 on 2023-10-30 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dishes',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='dish',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='restaurant.dish'),
            preserve_default=False,
        ),
    ]
