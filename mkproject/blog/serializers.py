from rest_framework import serializers
from .models import blog,Book



class blogserializer(serializers.ModelSerializer):
    class Meta:
        model = blog
        fields = '__all__'

# serializers.py


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'