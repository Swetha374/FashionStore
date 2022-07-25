from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
from functools import reduce

class HelloWorldView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"hello world"})

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"Good morning guys"})

class GoodAfternoonView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"Greetings":"Good afternoon"})

class GreetingsView(APIView):
    def get(self,request,*args,**kwargs):
        c_date=datetime.datetime.now()
        c_hour=c_date.hour
        msg=""
        if c_hour<12:
            msg="good morning"
        elif(c_hour<18):
            msg="good afternoon"
        elif(c_hour<24):
            msg="good night"
        return Response({"data":msg})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        n=request.data.get("num")
        res=n**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        num=request.data.get("num")
        fact=reduce(lambda n1,n2:n1*n2,range(1,num+1))
        return Response({"msg":fact})

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        wc={}
        words=text.split(" ")
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response({"data":wc})

