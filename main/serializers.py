from rest_framework import serializers

from main.models import CustomerPoint


class CustomerPointSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=26, required=False)
    customerId = serializers.CharField(max_length=26, source='customer_id')
    amount = serializers.IntegerField()
    rank = serializers.CharField(max_length=50),
    expiredDate = serializers.DateTimeField(required=False, source='expired_date')
    status = serializers.IntegerField()

    class Meta:
        model = CustomerPoint
        fields = ('id', 'customerId', 'amount', 'expiredDate', 'status')
