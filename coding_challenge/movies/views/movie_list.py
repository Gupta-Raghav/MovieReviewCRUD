from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.db.models import Avg
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListSerializer



class MovieListView(ListCreateAPIView):
    serializer_class = MovieListSerializer    
    def get_queryset(self):
        runtime = self.request.query_params.get('runtime',None)
        op = self.request.query_params.get('op', None)
        if runtime:
            if op:
                if op=='gt':
                    return Movie.objects.filter(runtime__gt=runtime).order_by("id")
                else:
                    return Movie.objects.filter(runtime__lt=runtime).order_by("id")
            return Movie.objects.filter(runtime=runtime).order_by("id")
        return Movie.objects.order_by("id")
    
class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all().prefetch_related("reviews").annotate(avg_rating= Avg("reviews__rating"))
    serializer_class = MovieSerializer
    lookup_field = 'id' 


    

