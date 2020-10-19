from rest_framework import serializers

from .models import Order


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user')
