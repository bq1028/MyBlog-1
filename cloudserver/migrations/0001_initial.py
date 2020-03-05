# Generated by Django 2.1.3 on 2019-10-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System_Monit',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cpu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cur_mem', models.IntegerField()),
                ('mem_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mem_all', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('time_stamp', models.BigIntegerField()),
            ],
        ),
    ]
