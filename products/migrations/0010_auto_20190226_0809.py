# Generated by Django 2.1.7 on 2019-02-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20190221_0656'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('sizeID', models.AutoField(primary_key=True, serialize=False)),
                ('sizeName', models.CharField(max_length=200)),
                ('sizeDescription', models.TextField(max_length=200)),
                ('sizeNotes', models.TextField(max_length=255)),
            ],
            options={
                'db_table': 'size',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='productSizes',
            field=models.ManyToManyField(to='products.Size'),
        ),
    ]
