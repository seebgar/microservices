from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId



# Create your views here.


'''
GET ALL - POST Reserva
'''
@api_view(["GET", "POST"])
def reservas(request):
    
    # MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    reservas = db['reservas']

    if request.method == "GET":
        result = []
        data = reservas.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                'fecha': str(dto['fecha']),
                'espacio': str(dto['espacio']),
                'pago': str(dtp['pago'])
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    

    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = reservas.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)




'''
GET ID - UPDATE Reserva
'''
@api_view(["GET", "POST"])
def reservasDetail(request, pk):

    #MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    reservas = db['reservas']
    
    if request.method == "GET":
        data = reservas.find({'_id': ObjectId(pk)})
        result = []
        for dto in data:
            jsonData ={
                'id': str(dto['_id']),
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result[0], safe=False)


    if request.method == "POST":
        data = JSONParser().parse(request)
        result = reservas.update(
            {'_id': ObjectId(pk)},
            {'$push': {'threshold': data}} # TODO Variables
        )
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        return JsonResponse(respo, safe=False)

        