# Generated by Django 3.2.8 on 2021-10-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('cart', '0002_alter_cartitem_product_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
