# Generated by Django 4.0.2 on 2022-04-15 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(blank=True, null=True, upload_to='static/image')),
                ('Uraian', models.CharField(default='', max_length=225)),
                ('Tanggal_Transaksi', models.CharField(default='', max_length=100)),
                ('Status', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
