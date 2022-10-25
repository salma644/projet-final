# Generated by Django 4.0.4 on 2022-06-24 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0008_hypervisordetails_vm'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypervisordetails',
            name='net',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appli.networkdetails'),
        ),
        migrations.AddField(
            model_name='virtualmachine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appli.userlist'),
        ),
    ]
