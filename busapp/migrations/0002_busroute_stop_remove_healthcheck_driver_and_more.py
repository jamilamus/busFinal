# Generated by Django 4.2.6 on 2023-10-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(default='Unknown', max_length=255)),
                ('route_length', models.DecimalField(decimal_places=2, default='Unknown', max_digits=10)),
                ('time_to_complete', models.PositiveIntegerField(default='Unknown')),
                ('stop_interval', models.PositiveIntegerField(default='Unknown')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_name', models.CharField(default='Unknown', max_length=255)),
                ('stop_interval', models.PositiveIntegerField(default='Unknown')),
                ('route', models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to='busapp.busroute')),
            ],
        ),
        migrations.RemoveField(
            model_name='healthcheck',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='bus',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='make',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='model',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='serial_number',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='routes',
        ),
        migrations.AddField(
            model_name='bus',
            name='backup_driver_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='backup_driver_1_for_buses', to='busapp.driver'),
        ),
        migrations.AddField(
            model_name='bus',
            name='backup_driver_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='backup_driver_2_for_buses', to='busapp.driver'),
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_number',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='bus',
            name='primary_driver_1',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, related_name='primary_driver_1_for_buses', to='busapp.driver'),
        ),
        migrations.AddField(
            model_name='bus',
            name='primary_driver_2',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, related_name='primary_driver_2_for_buses', to='busapp.driver'),
        ),
        migrations.AddField(
            model_name='driver',
            name='days_off',
            field=models.DateField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='driver',
            name='driver_name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='driver',
            name='health_condition',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='HealthCheck',
        ),
        migrations.DeleteModel(
            name='Inspection',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.AddField(
            model_name='bus',
            name='route',
            field=models.ForeignKey(default='Unknown', on_delete=django.db.models.deletion.CASCADE, to='busapp.busroute'),
        ),
        migrations.AddField(
            model_name='driver',
            name='assigned_routes',
            field=models.ManyToManyField(default='Unknown', to='busapp.busroute'),
        ),
    ]
