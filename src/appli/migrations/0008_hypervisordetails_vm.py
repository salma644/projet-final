# Generated by Django 4.0.4 on 2022-06-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0007_networkdetails_hyp_networkdetails_vm'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypervisordetails',
            name='vm',
            field=models.ManyToManyField(to='appli.virtualmachine'),
        ),
    ]
