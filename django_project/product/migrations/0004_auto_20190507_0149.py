# Generated by Django 2.1.5 on 2019-05-06 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_bill_bill_quatity'),
    ]

    operations = [
        migrations.CreateModel(
            name='billItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billItem_quatity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='bill',
            name='bill_product',
        ),
        migrations.RemoveField(
            model_name='bill',
            name='bill_quatity',
        ),
        migrations.AddField(
            model_name='billitem',
            name='billItem_bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.bill'),
        ),
        migrations.AddField(
            model_name='billitem',
            name='billItem_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]