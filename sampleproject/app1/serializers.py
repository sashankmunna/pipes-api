# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from app1.models import pipes

# Create a model serializer
class PipesSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = pipes
		fields = "__all__"
