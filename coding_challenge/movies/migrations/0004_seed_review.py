from django.db import migrations

def populate_db(apps, schema_editor):
    review = apps.get_model('movies', 'Review')
    review.objects.create(name="RG", rating=4, movie_id=1)
    review.objects.create(name="DR", rating=1, movie_id=1)
    review.objects.create(name="DR", rating=2, movie_id=2)
    review.objects.create(name="RG", rating=3, movie_id=2)

def empty_db(apps, schema_editor):
    review = apps.get_model('movies', 'Review')
    review.objects.using().filter(title__in=[
        "RG","DR"
    ]).delete()
    
class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_review'),  # Replace with the name of your previous migration
    ]

    operations = [
        migrations.RunPython(populate_db, empty_db),
    ]