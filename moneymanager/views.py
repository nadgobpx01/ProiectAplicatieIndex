from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.mail import EmailMessage
from datetime import timedelta
from django.db.models import Sum
from weasyprint import HTML

from .models import Transaction, Category
from .forms import TransactionForm, CategoryForm, DateRangeForm


class OverviewView(LoginRequiredMixin, TemplateView):
    template_name = 'moneymanager/overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = DateRangeForm(self.request.GET or None)
        end_date = now().date()
        start_date = end_date - timedelta(days=30)
        if form.is_valid():
            if form.cleaned_data.get('start_date'):
                start_date = form.cleaned_data['start_date']
            if form.cleaned_data.get('end_date'):
                end_date = form.cleaned_data['end_date']
        transactions = Transaction.objects.filter(user=self.request.user, date__range=(start_date, end_date))
        total_income = transactions.filter(category__is_income=True).aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = transactions.filter(category__is_income=False).aggregate(Sum('amount'))['amount__sum'] or 0
        sold = total_income - total_expense
        context.update({
            'form': form,
            'start_date': start_date,
            'end_date': end_date,
            'total_income': total_income,
            'total_expense': total_expense,
            'global_sold': sold,
            'global_username': self.request.user.username,
            'transactions': transactions.order_by('-date'),
        })
        return context


class ExportPdfView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = DateRangeForm(request.GET or None)
        end_date = now().date()
        start_date = end_date - timedelta(days=30)
        if form.is_valid():
            if form.cleaned_data.get('start_date'):
                start_date = form.cleaned_data['start_date']
            if form.cleaned_data.get('end_date'):
                end_date = form.cleaned_data['end_date']

        transactions = Transaction.objects.filter(user=request.user, date__range=(start_date, end_date))
        total_income = transactions.filter(category__is_income=True).aggregate(Sum('amount'))['amount__sum'] or 0
        total_expense = transactions.filter(category__is_income=False).aggregate(Sum('amount'))['amount__sum'] or 0
        sold = total_income - total_expense

        template = get_template("moneymanager/pdf_template.html")
        html = template.render({
            'transactions': transactions,
            'total_income': total_income,
            'total_expense': total_expense,
            'sold': sold,
            'start_date': start_date,
            'end_date': end_date,
            'user': request.user
        })

        pdf_file = HTML(string=html).write_pdf()
        filename = "raport_moneymanager.pdf"

        if request.GET.get('mode') == 'download':
            response = HttpResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response

        email = EmailMessage(
            subject="Raport Financiar MoneyManager",
            body="Vezi atasat raportul financiar în format PDF.",
            from_email=None,
            to=[request.user.email],
        )
        email.attach(filename, pdf_file, "application/pdf")
        email.send()

        return HttpResponseRedirect(reverse_lazy('moneymanager:overview'))


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    context_object_name = 'transactions'
    template_name = 'moneymanager/transaction_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')


class TransactionDetailView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'moneymanager/transaction_detail.html'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'moneymanager/transaction_form.html'
    success_url = reverse_lazy('moneymanager:transaction-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'moneymanager/transaction_form.html'
    success_url = reverse_lazy('moneymanager:transaction-list')


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'moneymanager/transaction_confirm_delete.html'
    success_url = reverse_lazy('moneymanager:overview')


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'moneymanager/category_list.html'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'moneymanager/category_detail.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'moneymanager/category_form.html'
    success_url = reverse_lazy('moneymanager:category-list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'moneymanager/category_form.html'
    success_url = reverse_lazy('moneymanager:category-list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'moneymanager/category_confirm_delete.html'
    success_url = reverse_lazy('moneymanager:category-list')
