from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

class FoodList(APIView):
    def get(self, request):
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)

class FoodDetail(APIView):
    def get_object(self, pk):
        try:
            return Food.objects.get(pk=pk)
        except Food.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    
    def get(self, request, pk):
        food = self.get_object(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def delete(self, request, pk):
        food = self.get_object(pk)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
