# Generated by Django 4.0.2 on 2022-04-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pembukuan_kas', '0002_alter_transaksi_tanggal_transaksi'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaksi',
            name='Nominal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
