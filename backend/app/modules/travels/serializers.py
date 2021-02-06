from rest_framework import serializers
# from app.modules.profiles.serializers import ProfileSerializer
from .models import Travels

class TravelSerializer(serializers.ModelSerializer):
    # author = ProfileSerializer(read_only=True)
    travel = serializers.CharField()

   

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
    def create(self, validated_data):
        driver = self.context.get('driver', None)

        print('************** create travel ser *******************')
        # print(validated_data.get('hashtags', []))
        # hashtags = validated_data.pop('hashtags', [])
        post = Post.objects.create(driver=driver, **validated_data)
        # for hashtag in hashtags:
        #     post.hashtags.add(hashtag)
        return post
    
    # def create(self, validated_data):
    #     author = self.context.get('author', None)

    #     print('************** create travel ser *******************')
    #     print(validated_data.get('hashtags', []))
    #     hashtags = validated_data.pop('hashtags', [])
    #     travel = Travel.objects.create(author=author, **validated_data)
    #     for hashtag in hashtags:
    #         travel.hashtags.add(hashtag)
    #     return travel

