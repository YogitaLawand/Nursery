# Generated by Django 5.0.7 on 2024-07-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nursery_app', '0002_alter_product_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
