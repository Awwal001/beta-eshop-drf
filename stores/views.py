from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from stores.models import Store
from stores.serializers import StoreSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getStores(request):
    users = Store.objects.all()
    serializer = StoreSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getOneStore(request, pk):
    store = Store.objects.get(id=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createStore(request):
    user = request.user
    data = request.data
    
    name = data['name']
    description = data['description']

    store = Store.objects.create(
        vendor=user,
        name=name,
        description=description
    )

    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateStore(request, pk):
    data = request.data
    store = Store.objects.get(id=pk)

    store.name = data['name']
    store.description = data['description']
    
    store.save()

    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteStore(request, pk):
    store = Store.objects.get(id=pk)
    store.delete()
    return Response('store Deleted')