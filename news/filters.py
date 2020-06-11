import django_filters

from news.models import Like


class LikeFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name="creation_date", lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name="creation_date", lookup_expr='lte')

    class Meta:
        model = Like
        fields = ['creation_date', 'user']