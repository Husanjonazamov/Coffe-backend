from rest_framework import serializers
from core.apps.api.models import ProductModel
from core.apps.api.serializers.category import BaseCategorySerializer


class BaseProductSerializer(serializers.ModelSerializer):
    category = BaseCategorySerializer(many=True)
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

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

    def get_title(self, obj):
        lang = self.context.get("lang", "uz")
        return getattr(obj, f"title_{lang}", obj.title)

    def get_description(self, obj):
        lang = self.context.get("lang", "uz")
        return getattr(obj, f"description_{lang}", obj.description)


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        pass


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        pass


class CreateProductSerializer(serializers.ModelSerializer):
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
