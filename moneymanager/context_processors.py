from .models import Transaction
from django.db.models import Sum

def global_context(request):
    if request.user.is_authenticated:
        income = Transaction.objects.filter(
            user=request.user, category__is_income=True
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        expense = Transaction.objects.filter(
            user=request.user, category__is_income=False
        ).aggregate(Sum('amount'))['amount__sum'] or 0

        return {
            'global_sold': income - expense,
            'global_username': request.user.username
        }
    return {'global_sold': 0, 'global_username': ''}
