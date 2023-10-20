# Generated by Django 4.2.6 on 2023-10-20 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0002_busroute_stop_remove_healthcheck_driver_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avtobus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avtobus_nömrəsi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Dayanacaq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('interval', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Surucu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('saglamliq_veziyyeti', models.CharField(max_length=255)),
                ('istirahət_günü', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Xett',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('uzunluq', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vaxt_tamamlayici', models.PositiveIntegerField()),
                ('interval', models.PositiveIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='assigned_routes',
        ),
        migrations.RemoveField(
            model_name='stop',
            name='route',
        ),
        migrations.DeleteModel(
            name='Bus',
        ),
        migrations.DeleteModel(
            name='BusRoute',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Stop',
        ),
        migrations.AddField(
            model_name='surucu',
            name='təyin_edilmis_xettlər',
            field=models.ManyToManyField(to='busapp.xett'),
        ),
        migrations.AddField(
            model_name='dayanacaq',
            name='xett',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.xett'),
        ),
        migrations.AddField(
            model_name='avtobus',
            name='rezerv_surucu_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rezerv_surucu_1_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AddField(
            model_name='avtobus',
            name='rezerv_surucu_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rezerv_surucu_2_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AddField(
            model_name='avtobus',
            name='xett',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busapp.xett'),
        ),
        migrations.AddField(
            model_name='avtobus',
            name='əsas_surucu_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='əsas_surucu_1_avtobuslar_üçün', to='busapp.surucu'),
        ),
        migrations.AddField(
            model_name='avtobus',
            name='əsas_surucu_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='əsas_surucu_2_avtobuslar_üçün', to='busapp.surucu'),
        ),
    ]
