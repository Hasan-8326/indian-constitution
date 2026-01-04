from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('history/', views.HistoryView.as_view(), name='history'),
    path('assembly/', views.ConstituentAssemblyView.as_view(), name='assembly'),
    path('preamble/', views.PreambleView.as_view(), name='preamble'),
    path('structure/', views.StructureView.as_view(), name='structure'),
    path('rights/', views.FundamentalRightsView.as_view(), name='rights'),
    path('amendments/', views.AmendmentsView.as_view(), name='amendments'),
    path('amendments/<int:pk>/', views.AmendmentDetailView.as_view(), name='amendment_detail'),
    path('judgments/', views.JudgmentsView.as_view(), name='judgments'),
    path('present-day/', views.PresentDayView.as_view(), name='present_day'),
    path('references/', views.ReferencesView.as_view(), name='references'),
]
