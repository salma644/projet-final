# Generated by Django 4.0.4 on 2022-06-07 00:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0003_alter_userlist_vm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='vm',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vm', to='appli.virtualmachine'),
        ),
    ]