# Generated by Django 4.2.3 on 2023-07-27 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esupport', '0010_oferta'),
    ]

    operations = [
        migrations.AddField(
            model_name='oferta',
            name='nombreProducto',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
