from rest_framework import serializers

# from conduit.apps.profiles.serializers import ProfileSerializer

from .models import Travels #, Comment, Tag
# from .relations import TagRelatedField


class TravelSerializer(serializers.ModelSerializer):
    # tagList = TagRelatedField(many=True, required=False, source='tags')

    # Django REST Framework makes it possible to create a read-only field that
    # gets it's value by calling a function. In this case, the client expects
    # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
    # `serializers.SerializerMethodField` is a good way to avoid having the
    # requirements of the client leak into our API.

    # createdAt = serializers.SerializerMethodField(method_name='get_created_at')
    # updatedAt = serializers.SerializerMethodField(method_name='get_updated_at')

    class Meta:
        model = Travels
        fields = (
            "Id",
            "driverId",
            "numPassengers",
            "date",
            "startTime",
            "finishTime",
            "city",
            "ubication",
            "postalCode",
            # "createdAt", Aqui no es
        )
