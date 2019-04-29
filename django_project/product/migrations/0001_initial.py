# Generated by Django 2.1.5 on 2019-04-28 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('city_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_list/')),
                ('product_price', models.PositiveIntegerField()),
                ('product_active', models.BooleanField(default=True)),
                ('product_description', models.TextField(blank=True, max_length=500, null=True)),
                ('product_quatity', models.PositiveIntegerField()),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
    ]
