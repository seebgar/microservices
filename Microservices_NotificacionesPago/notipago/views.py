from django.http import JsonResponse
from pymongo import MongoClient
import datetime
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser
from django.conf import settings
from bson.objectid import ObjectId



# Create your views here.


'''
GET ALL - POST Notificacion
'''
@api_view(["GET", "POST"])
def notificaciones(request):
    
    # MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    notificaciones = db['notificaciones']

    if request.method == "GET":
        result = []
        data = notificaciones.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                'texto': str(dto['texto'])
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    

    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = notificaciones.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)




'''
GET ID - UPDATE Notificacion
'''
@api_view(["GET", "POST"])
def notificacionesDetail(request, pk):

    #MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    notificaciones = db['notificaciones']
    
    if request.method == "GET":
        data = notificaciones.find({'_id': ObjectId(pk)})
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
        result = notificaciones.update(
            {'_id': ObjectId(pk)},
            {'$push': {'threshold': data}} # TODO Variables
        )
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        return JsonResponse(respo, safe=False)

        






'''
================================
'''







'''
GET ALL - POST Pagos
'''
@api_view(["GET", "POST"])
def pagos(request):
    
    # MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    pagos = db['pagos']

    if request.method == "GET":
        result = []
        data = pagos.find({})
        for dto in data:
            jsonData = {
                'id': str(dto['_id']),
                'costo': str(dto['costo'])
            }
            result.append(jsonData)
        client.close()
        return JsonResponse(result, safe=False)
    

    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = pagos.insert(data)
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        client.close()
        return JsonResponse(respo, safe=False)




'''
GET ID - UPDATE Pagos
'''
@api_view(["GET", "POST"])
def pagosDetail(request, pk):

    #MongoDB
    client = MongoClient(settings.DB_HOST, int(settings.DB_PORT))
    db = client[settings.MONGO_DB]
    db.authenticate(settings.MLAB_USER, settings.MLAB_PASSWORD)

    #List
    pagos = db['pagos']
    
    if request.method == "GET":
        data = pagos.find({'_id': ObjectId(pk)})
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
        result = pagos.update(
            {'_id': ObjectId(pk)},
            {'$push': {'costo': data}} # TODO Variables
        )
        respo ={
            "MongoObjectID": str(result),
            "Message": "nuevo objeto en la base de datos"
        }
        return JsonResponse(respo, safe=False)

        