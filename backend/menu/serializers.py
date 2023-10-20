from rest_framework import serializers

from .models import Category, Drink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DrinkSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()

    class Meta:
        model = Drink
        fields = [
            "title",
            "description",
            "price",
            "photo",
            "cat",
        ]
