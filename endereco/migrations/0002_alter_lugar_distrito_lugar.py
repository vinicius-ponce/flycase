# Generated by Django 4.2.1 on 2023-06-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='distrito_lugar',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
