# Generated by Django 3.2.4 on 2021-07-04 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0002_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='mensaje',
            new_name='descripcion',
        ),
    ]