# Generated by Django 4.2.6 on 2023-10-20 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0004_remove_avtobus_rezerv_surucu_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avtobus',
            name='rezerv_sürücü_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rezerv_sürücü_1_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AlterField(
            model_name='avtobus',
            name='rezerv_sürücü_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rezerv_sürücü_2_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AlterField(
            model_name='avtobus',
            name='xett',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.xett'),
        ),
        migrations.AlterField(
            model_name='avtobus',
            name='əsas_sürücü_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='əsas_sürücü_1_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AlterField(
            model_name='avtobus',
            name='əsas_sürücü_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='əsas_sürücü_2_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AlterField(
            model_name='dayanacaq',
            name='xett',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.xett'),
        ),
        migrations.AlterField(
            model_name='surucu',
            name='təyin_edilmis_xettlər',
            field=models.ManyToManyField(to='busapp.xett'),
        ),
    ]
