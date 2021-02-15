from rest_framework import serializers
from app.modules.profiles.serializers import ProfileSerializer
# from app.modules.travels.serializers import ValorationSerializer
from .models import Travels, Valoration
from .relations import ValorationRelatedField

#Valorations (comentarios...)
class ValorationSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    author = ProfileSerializer(required=False)
    createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    travel_slug = serializers.SlugField(required=False)
    # tagList = TagRelatedField(many=True, required=False, source='tags')
    # updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Valoration
        fields = (
            'slug',
            'author',
            'body',
            'createdAt',
            'travel_slug',
        )

    def create(self, validated_data):
        print("___________Create valoration serializer_________")
        travel = self.context['travel']
        # travel_slug = self.context['travel']
        author = self.context['author']  #El que hace el comentario

        return Valoration.objects.create(
            author=author, travel_slug=travel, **validated_data
        )

    def get_created_at(self, instance):
        return instance.createdAt.isoformat()

    # def get_updated_at(self, instance):
    #     return instance.updated_at.isoformat()

########################################################################################

class TravelSerializer(serializers.ModelSerializer):
    driver = ProfileSerializer(read_only=True) #driver es de tipo profile
    slug = serializers.SlugField(required=False)
    valorations = ValorationSerializer(many=True, read_only=True)

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
            'valorations',
        )
    def create(self, validated_data):  #Esto lo envia a la bd
        #data es lo del postman
        #validated_data tiene el driver
        driver = self.context.get('driver', None)
        travel = Travels.objects.create(driver=driver, **validated_data)
        return travel



    
