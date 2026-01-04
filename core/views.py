from django.views.generic import TemplateView, ListView, DetailView
from .models import Part, Article, Amendment, Judgment

class HomeView(TemplateView):
    template_name = 'home.html'

class HistoryView(TemplateView):
    template_name = 'history.html'

class ConstituentAssemblyView(TemplateView):
    template_name = 'assembly.html'

class PreambleView(TemplateView):
    template_name = 'preamble.html'

class StructureView(ListView):
    model = Article
    template_name = 'structure.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        # Optimized query for listing
        return Article.objects.select_related('part').all().order_by('id') # Or custom sort logic

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parts'] = Part.objects.all().order_by('id')
        return context

class FundamentalRightsView(TemplateView):
    template_name = 'rights.html'

class AmendmentsView(ListView):
    model = Amendment
    template_name = 'amendments.html'
    context_object_name = 'amendments'

class AmendmentDetailView(DetailView):
    model = Amendment
    template_name = 'amendment_detail.html'
    context_object_name = 'amendment'

class JudgmentsView(ListView):
    model = Judgment
    template_name = 'judgments.html'
    context_object_name = 'judgments'

class PresentDayView(TemplateView):
    template_name = 'present_day.html'

class ReferencesView(TemplateView):
    template_name = 'references.html'
