from django.shortcuts import render,redirect
from .forms import register,add_item
from .models import cash_male,cash_female
from django.contrib.auth.admin import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='login/')
def home(request):
    return render(request,'app/dashboad.html')

def register_page(request):
    if request.method =='POST':
        form = register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ចុះឈ្មោះទទួលបានជោគជ័យ !')
            return redirect('/login')
    else:
        form = register()
    return render(request,'app/register.html',{'form':form})


@login_required(login_url='/login')
def cash_male_page(request):
    base_male = cash_male.objects.filter(author=request.user.id)
    count = cash_male.objects.filter(author=request.user.id).count()
    page = Paginator(base_male,10)
    page_get = request.GET.get('page',1)
    page_list = page.page(page_get)
    dolloar = []
    reil = []
    for i in base_male:
        dolloar.append(i.dollar)
        reil.append(i.riel)
    total_dollar = sum(dolloar)
    total_riel = sum(reil)
    dollar = "${:,.2f}".format(total_dollar)
    riel = "{:,.0f}".format(total_riel)
    total_all = total_riel / 4100 + total_dollar
    total_all2 = "${:,.2f}".format(total_all)
    if request.method =='POST':
        quest_name = request.POST.get('guest_name')
        dollar1 = request.POST.get('dollar')
        riel = request.POST.get('riel')
        sex = request.POST.get('sex')
        user = User.objects.filter(username=request.user.username).first()
        add_new_item = cash_male.objects.create(guest_name=quest_name,dollar=dollar1,riel=riel,author=user,sex=sex)
        form = add_item(request.POST)
        if form.is_valid():
            add_new_item.save()
            return redirect('/cash-man')
    form = add_item()
    return render(request,'app/home.html',{'items':page_list,'form':form,'total_riel':riel,'total_dollar':dollar,'count':count,'total_all':total_all2,'page':page_list,'page_rang':page})

@login_required(login_url='/login')
def cash_woman_page(request):
    base_male = cash_female.objects.filter(author=request.user.id)
    count = cash_female.objects.filter(author=request.user.id).count()
    page = Paginator(base_male, 10)
    page_get = request.GET.get('page', 1)
    page_list = page.page(page_get)
    dolloar = []
    reil = []
    for i in base_male:
        dolloar.append(i.dollar)
        reil.append(i.riel)
    total_dollar = sum(dolloar)
    total_riel = sum(reil)
    dollar = "${:,.2f}".format(total_dollar)
    riel = "{:,.0f}".format(total_riel)
    total_all = total_riel / 4100 + total_dollar
    total_all2 = "${:,.2f}".format(total_all)
    if request.method == 'POST':
        quest_name = request.POST.get('guest_name')
        dollar1 = request.POST.get('dollar')
        riel = request.POST.get('riel')
        sex = request.POST.get('sex')
        user = User.objects.filter(username=request.user.username).first()
        add_new_item = cash_female.objects.create(guest_name=quest_name, dollar=dollar1, riel=riel, author=user, sex=sex)
        form = add_item(request.POST)
        if form.is_valid():
            add_new_item.save()
            return redirect('/cash-woman')
    form = add_item()
    return render(request, 'app/home.html',
                  {'items': page_list, 'form': form, 'total_riel': riel, 'total_dollar': dollar, 'count': count,
                   'total_all': total_all2, 'page': page_list, 'page_rang': page})



@login_required(login_url='/login')
def total_cash(request):
    base_male = cash_male.objects.filter(author=request.user.id)
    dolloar = []
    reil = []
    for i in base_male:
        dolloar.append(i.dollar)
        reil.append(i.riel)
    total_dollar = sum(dolloar)
    total_riel = sum(reil)
    total_all2 = total_riel / 4100 + total_dollar

    base_male = cash_female.objects.filter(author=request.user.id)
    dolloar = []
    reil = []
    for i in base_male:
        dolloar.append(i.dollar)
        reil.append(i.riel)
    total_dollar = sum(dolloar)
    total_riel = sum(reil)
    total_all = total_riel / 4100 + total_dollar
    x = total_all + total_all2
    y ="{:,.2f}".format(x)
    return render(request,'app/dashboad.html',{'total':y})


class deleteman(LoginRequiredMixin,DeleteView):
    model = cash_male
    success_url = "/cash-man"
    context_object_name = 'delete'

class deletewoman(LoginRequiredMixin,DeleteView):
    model = cash_female
    success_url = "/cash-woman"
    context_object_name = 'delete'

def delete_all(request):
        user = cash_male.objects.filter(author=request.user.id)
        user.delete()
        return redirect('/cash-man')


def delete_all_woman(request):
    user = cash_female.objects.filter(author=request.user.id)
    user.delete()
    return redirect('/cash-woman')
