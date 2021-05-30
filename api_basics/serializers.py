from rest_framework import serializers
from .models import Article

#  General Serializer
""" class ArticleSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self,validated_data):
        return Article.objects.create(validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance """


#  ModelSerializer (In this method, basic create and update method is already included)
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','description','email']

    ## This method wil overwrite the defalut save method for doing some validation.
    # def save(self):
        # pass

