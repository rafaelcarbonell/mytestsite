from rest_framework import serializers
from .models import Measure
from django.db import models


# Serializer for our entity Measure
class MeasureSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    timestamp = serializers.DateTimeField('timestamp')
    energy = serializers.DecimalField(max_digits=7, decimal_places=3)
    reactiveEnergy = serializers.DecimalField(max_digits=7, decimal_places=3)
    power = serializers.DecimalField(max_digits=7, decimal_places=3)
    maximeter = serializers.DecimalField(max_digits=7, decimal_places=3) 
    reactivePower = serializers.DecimalField(max_digits=7, decimal_places=3)
    voltage = serializers.DecimalField(max_digits=7, decimal_places=3)
    intensity = serializers.DecimalField(max_digits=7, decimal_places=3)
    powerFactor = serializers.DecimalField(max_digits=7, decimal_places=3)

    def create(self,id):
        """
        Create and return a new `Measure` instance, given the id.
        """
        return Measure.objects.create(**id)

    def update(self,instance, id):
        """
        Update and return an existing `Measure` instance, given the id.
        """
        instance.id = id.get('id', instance.id)
        instance.timestamp = id.get('timestamp', instance.timestamp)
        instance.energy = id.get('energy', instance.energy)
        instance.reactiveEnergy = id.get('reactiveEnergy', instance.reactiveEnergy)
        instance.power = id.get('power', instance.power)
        instance.maximeter = id.get('maximeter', instance.maximeter)
        instance.reactivePower = id.get('reactivePower', instance.reactivePower)
        instance.voltage = id.get('voltage', instance.voltage)
        instance.intensity = id.get('intensity', instance.intensity)
        instance.powerFactor = id.get('powerFactor', instance.powerFactor)

        instance.save()
        return instance
