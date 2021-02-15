from rest_framework import serializers
from app.modules.profiles.serializers import ProfileSerializer
from .models import Travels, Valoration
from .relations import ValorationRelatedField


class TravelSerializer(serializers.ModelSerializer):
    driver = ProfileSerializer(read_only=True) #driver es de tipo profile
    slug = serializers.SlugField(required=False)
    # valorationsList = ValorationRelatedField(many=True, required=False, source='valorations')
    # travel = serializers.CharField()

    class Meta:
        model = Travels
        fields = (
            'slug',
            'driver',
            'numPassengers',
            'date',
            'startTime',
            'finishTime',
            'city',               
            'ubication',
            'postalCode',
            # 'valorationsList',
            # 'valorations',
        )
    def create(self, validated_data):  #Esto lo envia a la bd
        #data es lo del postman
        #validated_data tiene el driver
        driver = self.context.get('driver', None)
        travel = Travels.objects.create(driver=driver, **validated_data)
        return travel


#Valorations (comentarios...)
class ValorationSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    author = ProfileSerializer(required=False)

    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    # updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Valoration
        fields = (
            'slug',
            'author',
            'body',
            'createdAt',
            'travel_slug',
            # 'updatedAt',
        )

    def create(self, validated_data):
        travel = self.context['travel']
        author = self.context['author']  #El que hace el comentario

        return Valoration.objects.create(
            author=author, travel_slug=travel, **validated_data
        )

    def get_created_at(self, instance):
        return instance.createdAt.isoformat()

    # def get_updated_at(self, instance):
    #     return instance.updated_at.isoformat()
    
