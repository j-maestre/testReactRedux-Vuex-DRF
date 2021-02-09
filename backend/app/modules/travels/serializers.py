from rest_framework import serializers
from app.modules.profiles.serializers import ProfileSerializer
from .models import Travels

class TravelSerializer(serializers.ModelSerializer):
    driver = ProfileSerializer(read_only=True) #driver es de tipo profile
    # slug = serializers.SlugField(required=False)
    # travel = serializers.CharField()

    class Meta:
        model = Travels
        fields = (
            # 'slug',
            'driver',
            'numPassengers',
            'date',
            'startTime',
            'finishTime',
            'city',               
            'ubication',
            'postalCode',
        )
    def create(self, validated_data):  #Esto lo envia a la bd
        #data es lo del postman
        #validated_data tiene el driver
        driver = self.context.get('driver', None)
        travel = Travels.objects.create(driver=driver, **validated_data)
        return travel
    
