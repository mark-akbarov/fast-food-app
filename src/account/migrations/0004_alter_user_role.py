# Generated by Django 4.2.3 on 2023-10-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_rename_type_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('waiter', 'Waiter'), ('customer', 'Customer')], default='customer', max_length=10),
        ),
    ]
