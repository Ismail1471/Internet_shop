# Generated by Django 4.2 on 2023-05-02 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_category_main_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=150, unique=True, verbose_name='Название товара')),
                ('description', models.TextField(verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Цена товара')),
                ('quantity', models.IntegerField(default=10, verbose_name='Кол-во товара')),
                ('is_available', models.BooleanField(default=True, verbose_name='В наличии')),
                ('slug', models.SlugField(default='')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.maincategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.product')),
            ],
        ),
    ]
