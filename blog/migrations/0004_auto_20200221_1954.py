# Generated by Django 2.1.7 on 2020-02-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200221_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
