# Generated by Django 3.2.5 on 2021-08-03 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='othersize',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]