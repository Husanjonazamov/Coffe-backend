from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.category import BaseCategorySerializer

class BaseProductSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer(many=True)
    
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "description",
            "category",
            "image",
            "price"
            
        ]


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
