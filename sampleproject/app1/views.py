
from rest_framework import viewsets

# import local data
from app1.serializers import PipesSerializer
from app1.models import pipes

# create a viewset
class pipes_view(viewsets.ModelViewSet):
	# define queryset
	queryset = pipes.objects.all()
	
	# specify serializer to be used
	serializer_class = PipesSerializer
