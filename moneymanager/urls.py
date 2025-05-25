from django.urls import path
from .views import (
    OverviewView, TransactionListView, TransactionDetailView,
    TransactionCreateView, TransactionUpdateView, TransactionDeleteView,
    CategoryListView, CategoryDetailView, CategoryCreateView,
    CategoryUpdateView, CategoryDeleteView, ExportPdfView
)

app_name = 'moneymanager'

urlpatterns = [
    path('overview/', OverviewView.as_view(), name='overview'),
    path('overview/export/', ExportPdfView.as_view(), name='export-pdf'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/add/', TransactionCreateView.as_view(), name='transaction-add'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/<int:pk>/edit/', TransactionUpdateView.as_view(), name='transaction-edit'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction-delete'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
