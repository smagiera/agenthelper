import datetime
from haystack import indexes
from helper.models import Policy, Client, Vehicle


class PolicyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    number = indexes.CharField(model_attr='number')
    vehicle = indexes.CharField(model_attr='vehicle', default='')
    property = indexes.CharField(model_attr='property', default='')
    client = indexes.CharField(model_attr='client')
    date_issued = indexes.DateTimeField(model_attr='date_issued')
    date_start = indexes.DateTimeField(model_attr='date_start')
    date_end = indexes.DateTimeField(model_attr='date_end')

    def get_model(self):
        return Policy

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date_issued__lte=datetime.datetime.now())

class VehicleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    reg_number = indexes.CharField(model_attr='reg_number')
    make = indexes.CharField(model_attr='make')
    model = indexes.CharField(model_attr='model')
    vin = indexes.CharField(model_attr='vin')
    owner = indexes.CharField(model_attr='owner')

    def get_model(self):
        return Vehicle

class ClientIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    id = indexes.CharField(model_attr='pesel_or_regon')

    def get_model(self):
        return Client
