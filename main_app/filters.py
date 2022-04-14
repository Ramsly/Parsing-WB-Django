from django_filters import rest_framework as filters

from main_app.models import Card


class TimeFilter(filters.FilterSet):
    data = filters.RangeFilter()

    class Meta:
        model = Card
        fields = ['date']
