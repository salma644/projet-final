# Generated by Django 4.0.4 on 2022-06-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HypervisorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=100)),
                ('hostname', models.CharField(editable=False, max_length=100, null=True)),
                ('uuid', models.CharField(editable=False, max_length=100, null=True)),
                ('memory', models.IntegerField()),
                ('cpucount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NetworkDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=50)),
                ('emplacement', models.CharField(max_length=300)),
                ('netmask', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Virtualmachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Statut', models.CharField(max_length=50)),
                ('RAM', models.IntegerField()),
                ('Vcpus', models.IntegerField()),
            ],
        ),
    ]
