# Generated by Django 4.0 on 2023-02-01 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_company_ads_companyname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='companyname',
        ),
        migrations.AddField(
            model_name='ads',
            name='companyLink',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
