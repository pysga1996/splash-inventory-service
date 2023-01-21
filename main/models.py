import ulid
from django.db import models


# Create your models here.


class CustomerPoint(models.Model):
    id = models.CharField(primary_key=True, max_length=26, )
    customer_id = models.CharField(max_length=26)
    amount = models.BigIntegerField()
    rank = models.CharField(),
    expired_date = models.DateTimeField(null=True)
    status = models.SmallIntegerField()

    def save(self, *args, **kwargs):
        self.id = str(ulid.ULID())
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'customer_point'


class CustomerVoucher(models.Model):
    customer_id = models.CharField(max_length=26)
    voucher_id = models.CharField(max_length=26)
    available = models.IntegerField()
    used = models.IntegerField()

    class Meta:
        db_table = 'customer_voucher'


class ShopVoucher(models.Model):
    shop_id = models.CharField(max_length=26)
    voucher_id = models.CharField(max_length=26)
    quantity = models.BigIntegerField()

    class Meta:
        db_table = 'shop_voucher'


class Voucher(models.Model):
    id = models.CharField(primary_key=True, max_length=26)
    name = models.CharField(max_length=50)
    condition_id = models.CharField(max_length=26)
    expression_id = models.CharField(max_length=26)
    expired_date = models.DateTimeField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    status = models.SmallIntegerField()

    class Meta:
        db_table = 'voucher'


class VoucherCondition(models.Model):
    id = models.CharField(primary_key=True, max_length=26)
    device_types = models.CharField(max_length=100)
    payment_method_codes = models.CharField(max_length=100)
    delivery_partner_codes = models.CharField(max_length=100)
    min_amount = models.DecimalField(max_digits=20, decimal_places=2)
    max_amount = models.DecimalField(max_digits=20, decimal_places=2)
    max_usage = models.IntegerField()
    status = models.SmallIntegerField()

    class Meta:
        db_table = 'voucher_condition'


class VoucherExpression(models.Model):
    id = models.BigAutoField(primary_key=True)
    discount_amount = models.DecimalField(max_digits=20, decimal_places=2)
    discount_unit = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    status = models.SmallIntegerField()

    class Meta:
        db_table = 'voucher_expression'
