# Generated by Django 4.1.6 on 2023-02-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
