# Generated by Django 3.2.7 on 2021-10-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('On', 'online'), ('Bu', 'bussy'), ('Of', 'offline')], max_length=2, null=True),
        ),
    ]
