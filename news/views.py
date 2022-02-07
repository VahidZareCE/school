from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from news.serializers import NewsSerializer
from news.models import News

class ListCreateNews(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(origin=self.request.user)

class UpdateDeleteNews(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
