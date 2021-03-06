# Generated by Django 4.0.5 on 2022-06-22 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='exposure_start',
        ),
        migrations.AddField(
            model_name='product',
            name='create_start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
