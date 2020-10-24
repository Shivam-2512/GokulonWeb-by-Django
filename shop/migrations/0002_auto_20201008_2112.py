# Generated by Django 3.1 on 2020-10-08 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='publish_date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcatagory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
