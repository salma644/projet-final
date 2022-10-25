# Generated by Django 4.0.4 on 2022-06-06 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField(default='')),
                ('vm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.virtualmachine')),
            ],
        ),
    ]