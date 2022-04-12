#from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from plants.models import Plants
from plants.serializers import PlantsSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "plants/index.html")

#def index(request):
 #   return HttpResponse("Hello, world. You're at the plants index.")

def index(request):
    print("------------------------- I AM HERE")
    queryset = Plants.objects.all()
    return render(request, "plants/index.html", {'plants': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'plants/index.html'

    def get(self, request):
        queryset = Plants.objects.all()
        return Response({'plants': queryset})


class list_all_plants(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'plants/plant_list.html'

    def get(self, request):
        queryset = Plants.objects.all()
        return Response({'plants': queryset})


# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def plant_list(request):
    if request.method == 'GET':
        plants = Plants.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            plants = plants.filter(title__icontains=title)

        plant_serializer = PlantsSerializer(plants, many=True)
        return JsonResponse(plant_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        plant_data = JSONParser().parse(request)
        plant_serializer = PlantsSerializer(data=plant_data)
        if plant_serializer.is_valid():
            plant_serializer.save()
            return JsonResponse(plant_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(plant_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Plants.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Plants were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def plant_detail(request, pk):
    try:
        plant = Plants.objects.get(pk=pk)
    except Plants.DoesNotExist:
        return JsonResponse({'message': 'The plant does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        plant_serializer = PlantsSerializer(plant)
        return JsonResponse(plant_serializer.data)

    elif request.method == 'PUT':
        plant_data = JSONParser().parse(request)
        plant_serializer = PlantsSerializer(plant, data=plant_data)
        if plant_serializer.is_valid():
            plant_serializer.save()
            return JsonResponse(plant_serializer.data)
        return JsonResponse(plant_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plant.delete()
        return JsonResponse({'message': 'Plant was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def plant_list_published(request):
    plants = Plants.objects.filter(published=True)

    if request.method == 'GET':
        plant_serializer = PlantsSerializer(plants, many=True)
        return JsonResponse(plant_serializer.data, safe=False)