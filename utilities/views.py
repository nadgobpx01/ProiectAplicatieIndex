from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ConsumptionForm
from .models import Consumption

@login_required
def add_consumption(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # Caută ultima intrare pentru același tip și utilizator
            last_entry = Consumption.objects.filter(tip=new_entry.tip, user=request.user).order_by('-created_at').first()
            new_entry.user = request.user
            new_entry.index_vechi = last_entry.index_nou if last_entry else 0
            new_entry.total_consum = new_entry.index_nou - new_entry.index_vechi
            new_entry.total_cost = new_entry.total_consum * new_entry.pret_unitar
            new_entry.save()
            return redirect('consumption_success')  # creezi această pagină sau redirectezi la listare
    else:
        form = ConsumptionForm()
    return render(request, 'utilities/add_consumption.html', {'form': form})
