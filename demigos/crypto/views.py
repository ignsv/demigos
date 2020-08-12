from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .forms import CreatePairForm

from .models import Pair

class IndexPageView(View):
    template_name = "web/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': CreatePairForm, 'objects': Pair.objects.all()})

    def post(self, request, *args, **kwargs):
        form = CreatePairForm(data=request.POST)
        if form.is_valid():
            pair = form.save()
            return redirect('pair-detail', pk=pair.id)

        return render(request, self.template_name, {'form': form, 'objects': Pair.objects.all()})


class PairDetailView(DetailView):
    model = Pair
    template_name = "web/detail.html"
