from rest_framework import serializers
from .models import Posts

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=('id','title','author','pub_date','contents')