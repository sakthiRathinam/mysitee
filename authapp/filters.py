import django_filters
from .models import inVoice
class poFilter(django_filters.FilterSet):
	class Meta:
		model = inVoice
		fields = ['ponumber']