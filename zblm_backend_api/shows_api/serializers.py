from rest_framework import serializers 
from .models import Show

class ShowSerializer(serializers.ModelSerializer): 
# serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Show 
        # tell django which model to use
        fields = ('id', 'venue', 'date', 'time', 'description', 'image', 'location', 'coverPrice', 'other',) 
        # tell django which fields to include
