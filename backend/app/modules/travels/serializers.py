from rest_framework import serializers
from app.modules.profiles.serializers import ProfileSerializer
from .models import Travels

class TravelSerializer(serializers.ModelSerializer):
    driver = ProfileSerializer(read_only=True) #driver es de tipo profile
    # travel = serializers.CharField()

    class Meta:
        model = Travels
        fields = (
            # 'id',
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
    
    # def create(self, validated_data):
    #     author = self.context.get('author', None)

    #     print('************** create travel ser *******************')
    #     print(validated_data.get('hashtags', []))
    #     hashtags = validated_data.pop('hashtags', [])
    #     travel = Travel.objects.create(author=author, **validated_data)
    #     for hashtag in hashtags:
    #         travel.hashtags.add(hashtag)
    #     return travel

