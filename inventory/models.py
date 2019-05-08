from django.db import models, connection
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.postgres.indexes import GinIndex


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, default='', blank=True)
    country = models.CharField(max_length=128, default='', blank=True)


class Item(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name='item', on_delete=models.PROTECT)
    name = models.CharField(max_length=128, default='', blank=True)
    description = models.CharField(max_length=128, default='', blank=True)
    cost = models.IntegerField()
    inventor = models.CharField(max_length=128, default='', blank=True)

    class Meta:
        indexes = (
          models.Index(fields=['description']),
          GinIndex(name='inventor_trigram_index', fields=['inventor'], opclasses=['gin_trgm_ops']),
        )

    @staticmethod
    def search_by_inventor(query, queryset=None):
        """Searches items by inventor using trigram similarity

        Trigram Similarity:
        https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/lookups/#std:fieldlookup-trigram_similar
        https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/search/#trigramsimilarity

        Args:
            query (string): the string to use to query the inventor. e.g. "sps"

        Returns:
            queryset: the queryset of all items whose inventor is similar to the query

        """
        qs = queryset if queryset is not None else Item.objects.all()

        # From https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/search/#trigramsimilarity
        qs = Item.objects.annotate(
            similarity=TrigramSimilarity('inventor', query),
        ).filter(similarity__gt=0.2).order_by('-similarity')

        #trigram_limit = 0.2
        #with connection.cursor() as cursor:
        #    cursor.execute(f"SELECT set_limit({trigram_limit});")

        #qs = qs.annotate(
        #    relevance=TrigramSimilarity('inventor', query),
        #).filter(inventor__trigram_similar=query).order_by('-relevance')

        return qs


