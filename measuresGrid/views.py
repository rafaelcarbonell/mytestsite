from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from measuresGrid.models import Measure
from measuresGrid.serializers import MeasureSerializer
import csv
import os
from datetime import datetime
from decimal import Decimal

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Is exent of csrf security
@csrf_exempt
def measure_list(request):
    # List all measures, or create a new measure.
    if request.method == 'GET':
        measures = Measure.objects.all()
        serializer = MeasureSerializer(measures, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MeasureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

#Is exent of csrf security
@csrf_exempt
def measure_detail(request, pk):
    # Retrieve, update or delete a measure.
    try:
        measure = Measure.objects.get(pk=pk)
    except Measure.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MeasureSerializer(measure)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MeasureSerializer(measure, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        measure.delete()
        return HttpResponse(status=204)

def index(request):
    # absolute dir the script is in
    script_dir = os.path.dirname(__file__) 
    # relative dir of the CSV file
    rel_path = "reports/Monitoring report.csv"
    # final path
    abs_file_path = os.path.join(script_dir, rel_path)

    # we read the data form CSV file splited each row by commas
    dataReader = csv.reader(open(abs_file_path), delimiter=',', quotechar='"')

    # boolean variable to avoid reading headers from excel
    headerRow = True

    # index to give a certain id to measures in DB
    i = 1

    # loop for saving measures into db if the rows from CSV file have correct format
    for row in dataReader:

        if(headerRow == False):
            try:
                m=Measure()
                m.id = i
                m.timestamp=datetime.strptime(row[0],'%d %b %Y %H:%M:%S') 
                m.energy=row[1]
                m.reactiveEnergy=row[2]
                m.power=row[3]
                m.maximeter=row[4]
                m.reactivePower=row[5]
                m.voltage=row[6]
                m.intensity=row[7]
                m.powerFactor=row[8]
                m.save()  
                i = i+1
            except ValueError:
                raise ValueError("Incorrect data format in CSV file at row number %d",i+1)
        
            headerRow = False

    # Number of measures in DB
    num_measures=Measure.objects.all().count()

    # Measures from DB
    measures= Measure.objects.all()
    
    # Rendering HTML template index.html with our two variables for measures
    return render(
        request,
        'index.html',
        context={'num_measures':num_measures,'measures':measures},
    )