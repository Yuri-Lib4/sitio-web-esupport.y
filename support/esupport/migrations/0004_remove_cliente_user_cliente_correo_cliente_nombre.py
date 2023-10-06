# Generated by Django 4.2.3 on 2023-07-25 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esupport', '0003_rename_categoriaproducto_marcaproducto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='user',
        ),
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
