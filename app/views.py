from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import RegisterForm, AddItemForm
from .models import CashMale, CashFemale

@login_required(login_url='login/')
def home(request):
    return render(request, 'app/dashboard.html')

def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ចុះឈ្មោះទទួលបានជោគជ័យ !')
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})

@login_required(login_url='/login')
def cash_page(request, model):
    items = model.objects.filter(author=request.user)
    count = items.count()
    paginator = Paginator(items, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)

    total_dollar = sum(item.dollar for item in items)
    total_riel = sum(item.riel for item in items)
    total_all = total_riel / 4100 + total_dollar

    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.author = request.user
            new_item.save()
            return redirect(request.path)
    else:
        form = AddItemForm()

    context = {
        'items': page_obj,
        'form': form,
        'total_riel': "{:,.0f}".format(total_riel),
        'total_dollar': "${:,.2f}".format(total_dollar),
        'count': count,
        'total_all': "${:,.2f}".format(total_all),
        'page': page_obj,
        'page_range': paginator.page_range,
    }
    return render(request, 'app/home.html', context)

@login_required(login_url='/login')
def cash_male_page(request):
    return cash_page(request, CashMale)

@login_required(login_url='/login')
def cash_female_page(request):
    return cash_page(request, CashFemale)

@login_required(login_url='/login')
def total_cash(request):
    male_total = sum(item.dollar + item.riel / 4100 for item in CashMale.objects.filter(author=request.user))
    female_total = sum(item.dollar + item.riel / 4100 for item in CashFemale.objects.filter(author=request.user))
    total = male_total + female_total
    return render(request, 'app/dashboard.html', {'total': "${:,.2f}".format(total)})

class DeleteCashItem(LoginRequiredMixin, DeleteView):
    context_object_name = 'delete'

    def get_success_url(self):
        return self.success_url

class DeleteCashMale(DeleteCashItem):
    model = CashMale
    success_url = "/cash-man"

class DeleteCashFemale(DeleteCashItem):
    model = CashFemale
    success_url = "/cash-woman"

@login_required(login_url='/login')
def delete_all(request, model, redirect_url):
    model.objects.filter(author=request.user).delete()
    return redirect(redirect_url)

@login_required(login_url='/login')
def delete_all_male(request):
    return delete_all(request, CashMale, '/cash-man')

@login_required(login_url='/login')
def delete_all_female(request):
    return delete_all(request, CashFemale, '/cash-woman')
