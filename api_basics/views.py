from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Article
from .serializers import ArticleSerializers

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets


# Create your views here.


#################### Method : 1 - Function Based API Views #################################
""" @csrf_exempt
def article(request):
    if request.method == 'GET':
        return article_list(request)
    elif request.method == 'POST': 
        return article_create(request)

def article_list(request):
    article_list = Article.objects.all()
    serializer = ArticleSerializers(article_list, many=True) ## Get data from article , just pass the article insatance. No need data parameter
    return JsonResponse(serializer.data,safe=False)

def article_create(request):
    data = JSONParser().parse(request)
    serializer = ArticleSerializers(data=data) ## To pass data to serializer ,Need to use data parameter

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request,pk):

    try:
        article = Article.objects.get(pk=pk)
    
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        return article_detail_get(article)
    elif request.method == 'PUT': 
        return article_update(request,article)
    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)

def article_detail_get(article):
    serializer = ArticleSerializers(article)
    return JsonResponse(serializer.data)

def article_update(request,article):
    data = JSONParser().parse(request)
    serializer = ArticleSerializers(article,data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse(serializer.errors, status=400)

 """


#################### Method : 2 - Web browser Based API View (api_view() decorator) #################################

""" @api_view(['GET','POST']) 
def article(request):
    if request.method == 'GET':
        return article_list(request)
    elif request.method == 'POST': 
        return article_create(request)

def article_list(request):
    article_list = Article.objects.all()
    serializer = ArticleSerializers(article_list, many=True) ## Get data from article , just pass the article insatance. No need data parameter
    # return JsonResponse(serializer.data,safe=False)
    return Response(serializer.data)

def article_create(request):
    # data = JSONParser().parse(request)
    # serializer = ArticleSerializers(data=data) ## To pass data to serializer ,Need to use data parameter

    serializer = ArticleSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE']) 
def article_detail(request,pk):

    try:
        article = Article.objects.get(pk=pk)
    
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return article_detail_get(article)
    elif request.method == 'PUT': 
        return article_update(request,article)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def article_detail_get(article):
    serializer = ArticleSerializers(article)
    return Response(serializer.data)

def article_update(request,article):
    # data = JSONParser().parse(request)
    serializer = ArticleSerializers(article,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


#################### Method : 3 - Class Based API View #################################

""" class ArticleAPIView(APIView):

    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """

#################### Method : 4 - Generic Class Based API View n Mixins #################################

""" class ArticleGenericAPIView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin):

    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
       return self.list(request)
            

    def post(self,request):
        return self.create(request)


class ArticleDetailGenericAPIView(generics.GenericAPIView,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    lookup_field = 'id'

    def get(self, request, id = None):
        return self.retrieve(request,id)

    def put(self,request,id):
        return self.update(request,id=id)

    def delete(self,request, id):
        return self.destroy(request,id=id) """


#################### Method : 5 - Viewsets Class #################################

""" class ArticleViewSets(viewsets.ViewSet):

    def list(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        # article = Article.objects.get(pk)
        articles = Article.objects.all()
        article = get_object_or_404(articles,pk=pk)
        serializer = ArticleSerializers(article)
        return Response(serializer.data)

    def update(self,request,pk=None):
        article = Article.objects.get(pk)
        serializer = ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  """


#################### Method : 6 - Generic Viewsets Class with mixins #################################

""" class ArticleGenericViewSets(viewsets.GenericViewSet, 
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin
                            ):

    serializer_class = ArticleSerializers
    queryset = Article.objects.all(); """


#################### Method : 6 - Model Viewsets (No need mixin becuase internally this viewset extend genericviewset and mixins) #################################
class ArticleModelViewSets(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()