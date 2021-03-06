# Generated by Django 3.0.8 on 2020-08-08 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('p', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='one_click_puchasing',
            field=models.BooleanField(default=False),
        ),
    ]
