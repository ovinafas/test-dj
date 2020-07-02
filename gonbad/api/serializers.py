from rest_framework import serializers
from gonbad.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'name', 'active')

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'title', 'description', 'price', 'quantity', 'cover', 'category', 'recommended')