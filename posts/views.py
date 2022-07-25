from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import users,blogs

class PostView(APIView):

    def get(self,request,*args,**kwargs):
        if "limit" in request.query_params:
            limit=int(request.query_params.get("limit"))
            data=blogs[0:limit]
            return Response(data=data)

        if "liked_by" in request.query_params:
            id=int(request.query_params.get("liked_by"))
            liked_post=[blog for blog in blogs if id in blog["liked_by"]]
            return Response(data=liked_post)


        return Response({"data":blogs})

    def post(self,request,*args,**kwargs):
        blog=request.data
        blogs.append(blog)
        return Response(data=blog)

#url: social/posts/{pid}
class PostDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==pid].pop()
        return Response(data=blog)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        blog=[b for b in blogs if b["postId"]==id].pop()
        blogs.remove(blog)
        return Response(data=blog)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("pid")
        post=[p for p in blogs if p["postId"]==id].pop()
        post.update(request.data)
        return Response(data=post)

    #url: social/posts/likes/<int:post





