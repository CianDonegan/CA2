from django.urls import path
from .views import ProdCat, ProdDetail

app_name = 'shop'


""" About to put in the slug on the urls but i dont think its the correct thing to do or right way to go about it"""

urlpatterns = [                                                                                                 
    path('', ProdCat.as_view(), name = 'allProdCat'),
    path('<uuid:category_id>/', ProdCat.as_view(), name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', ProdDetail.as_view(), name = 'prod_detail'),
]