import datetime
from ..models import Measurement
from variables.models import Variable
from django.db import models

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def create_measurement(mea):
    print("Empieza la funcion para crear")
    measurement = Measurement(
        variable = Variable.objects.get(pk=int(mea["variable"])),
        value = mea["value"],
        unit = mea["unit"],
        place = mea["place"],
        dateTime = models.DateTimeField(mea["dateTime"])
    )
    measurement.save()
    return measurement

def update_measurement(mea_pk, new_mea):
    print("empieza la funcion que actualiza un mea")
    measurement = get_measurement(mea_pk)
    measurement.variable = Variable.objects.get(pk=int(new_mea["variable"]))
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.place = new_mea["place"]
    measurement.dateTime = datetime.datetime.strptime(new_mea["dateTime"], '%Y-%m-%dT%H:%M:%S.%fZ')
    measurement.save()
    return measurement

def delete_measurement(mea_pk):
    measurement = get_measurement(mea_pk)
    measurement.delete()
    return measurement