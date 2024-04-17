from rest_framework import serializers

from movies.models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = (
            "name",
            "rating",
        )

class MovieSerializer(serializers.ModelSerializer):
    formatted_runtime = serializers.SerializerMethodField()
    reviews =  ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "formatted_runtime",
            "reviews",
            "avg_rating",
            "release_date",
        )
    def get_formatted_runtime (self, obj):
        hours = obj.runtime // 60
        minutes = obj.runtime % 60
        return (f"{hours}:{minutes:02}")
    
    def get_avg_rating (self, obj):
        val = getattr(obj,"avg_rating")
        return 0 if not val else val

class MovieListSerializer(serializers.ModelSerializer):
    reviews =  ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "runtime",
            "reviews",
            "release_date",
        )