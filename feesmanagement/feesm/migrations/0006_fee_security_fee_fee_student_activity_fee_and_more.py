# Generated by Django 4.0.4 on 2022-05-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesm', '0005_rename_collected_fee_fee_current_amount_deposited_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='security_fee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fee',
            name='student_activity_fee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fee',
            name='university_fee',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
