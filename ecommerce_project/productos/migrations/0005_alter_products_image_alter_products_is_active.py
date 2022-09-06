# Generated by Django 4.1 on 2022-09-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
