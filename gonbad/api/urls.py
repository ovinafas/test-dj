from django.urls import path

from .views import ProductListView, ProductDetail, RecommendedProducts , CategoryList, CategoriesList

urlpatterns = [
	path('products/', ProductListView.as_view()),
	path('products/<int:pk>/', ProductDetail.as_view()),
	path('recommended/', RecommendedProducts.as_view()),
	path('cat/', CategoryList.as_view(), name='cat'),
	path('categories/', CategoriesList.as_view()),
]