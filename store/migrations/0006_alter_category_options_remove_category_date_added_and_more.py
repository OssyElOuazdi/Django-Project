# Generated by Django 5.0.1 on 2024-02-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_category_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='num_ratings',
        ),
        migrations.AddField(
            model_name='category',
            name='cate_name',
            field=models.CharField(default='Uncategorized', max_length=60),
        ),
    ]