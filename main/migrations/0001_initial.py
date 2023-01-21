# Generated by Django 3.2.8 on 2023-01-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPoint',
            fields=[
                ('id', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=26)),
                ('amount', models.BigIntegerField()),
                ('expired_date', models.DateTimeField(null=True)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'customer_point',
            },
        ),
        migrations.CreateModel(
            name='CustomerVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(max_length=26)),
                ('voucher_id', models.CharField(max_length=26)),
                ('available', models.IntegerField()),
                ('used', models.IntegerField()),
            ],
            options={
                'db_table': 'customer_voucher',
            },
        ),
        migrations.CreateModel(
            name='ShopVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_id', models.CharField(max_length=26)),
                ('voucher_id', models.CharField(max_length=26)),
                ('quantity', models.BigIntegerField()),
            ],
            options={
                'db_table': 'shop_voucher',
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('condition_id', models.CharField(max_length=26)),
                ('expression_id', models.CharField(max_length=26)),
                ('expired_date', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'voucher',
            },
        ),
        migrations.CreateModel(
            name='VoucherCondition',
            fields=[
                ('id', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('device_types', models.CharField(max_length=100)),
                ('payment_method_codes', models.CharField(max_length=100)),
                ('delivery_partner_codes', models.CharField(max_length=100)),
                ('min_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('max_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('max_usage', models.IntegerField()),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'voucher_condition',
            },
        ),
        migrations.CreateModel(
            name='VoucherExpression',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('discount_unit', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('status', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'voucher_expression',
            },
        ),
    ]
