from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView

from .models import Pair

class IndexPageView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Pair.objects.all()
        return context


class PairDetailView(DetailView):
    model = Pair
    template_name = "web/detail.html"
