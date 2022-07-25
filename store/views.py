from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from store.models import products

#url: localhost:8000/store/product
class ProductsView(APIView):
    def get(self,request,*args,**kwargs):   #to get limited products
        if 'limit' in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=products[0:limit]
            return Response(data=data)
        return Response(data=products)

    def post(self,request,*args,**kwargs):
        prod=request.data
        products.append(prod)
        return Response(data=prod)


#url:localhost:8000/store product/{proid}
class ProductDetailView(APIView):
    def get(self,request,*args,**kwargs):
        prod_id=kwargs.get("proid")
        pro_duct=[p for p in products if p["id"]==prod_id]
        return Response(data=pro_duct)

    def delete(self,request,*args,**kwargs):
        pro_id=kwargs.get("proid")
        pro=[p for p in products if p["id"]==pro_id].pop()
        products.remove(pro)
        return Response(data=pro)

    def put(self,request,*args,**kwargs):
        pro_id=kwargs.get("proid")
        pro=[p for p in products if p["id"]==pro_id].pop()
        pro.update(request.data)
        return Response(data=pro)




