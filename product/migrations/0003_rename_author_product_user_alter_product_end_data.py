# Generated by Django 4.0.5 on 2022-06-21 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_author_alter_product_end_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='end_data',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 19, 20, 29, 30, 96516)),
        ),
    ]
