import django_filters
from django_filters.filters import CharFilter
from .models import *


class VisitorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')

    class Meta:
        model = Visitor
        fields = ["name"]


class ContractorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains')

    class Meta:
        model = Contractor
        fields = ["name"]
