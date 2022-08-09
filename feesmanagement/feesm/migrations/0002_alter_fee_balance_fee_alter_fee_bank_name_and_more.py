# Generated by Django 4.0.4 on 2022-05-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feesm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='Balance_fee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='class_batch',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='collected_fee',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='credit_date_in_bank',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='drawn_on_bank_name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='fee',
            name='fee_deposited_at_university',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='instrument_no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='mob_no',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='mode_of_payment',
            field=models.CharField(default='0', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='nimcet_cet_rank',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='receipt_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='remarks',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='fee',
            name='transaction_date_of_ch_dd',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='fee',
            name='university_enrollment_no',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
