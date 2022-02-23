from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import Organization, Key
from .forms import OrganizationForm, KeyForm
from .filters import KeyFilter

menu = [{'title': 'Организации', 'url_name': 'orgs'},
        {'title': 'Ключи', 'url_name': 'keys'}
        ]


class OrganizationHome(ListView):
    model = Organization
    template_name = 'organization/organization.html'
    context_object_name = 'organizations'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Организации'
        return context


def index(request):
    keys_list = Key.objects.all()
    key_filter = KeyFilter(request.GET, queryset=keys_list)
    context = {
        'keys': keys_list,
        'menu': menu,
        'title': 'Главная страница',
        'filter': key_filter
    }
    return render(request, 'organization/key.html', context=context)


# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)
#
# 	orders = customer.order_set.all()
# 	order_count = orders.count()
#
# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs
#
# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

class KeyHome(ListView):
    model = Key
    template_name = 'organization/key.html'
    context_object_name = 'keys'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Ключи'
        return context


def delete_org(request, pk):
    organization = Organization.objects.get(id=pk)
    if request.method == "POST":
        organization.delete()
        return redirect('/')

    context = {'organization': organization}
    return render(request, 'organization/del_org.html', context)


def create_org(request):
    form = OrganizationForm()
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'organization/create_entity.html', context)


def update_org(request, pk):
    organization = Organization.objects.get(id=pk)
    form = OrganizationForm(instance=organization)

    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'organization/create_entity.html', context)


def delete_key(request, pk):
    key = Key.objects.get(id=pk)
    if request.method == "POST":
        key.delete()
        return redirect('/keys/')

    context = {'key': key}
    return render(request, 'organization/del_key.html', context)


def create_key(request):
    form = KeyForm()
    if request.method == 'POST':
        form = KeyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keys/')

    context = {'form': form}
    return render(request, 'organization/create_entity.html', context)


def update_key(request, pk):
    key = Key.objects.get(id=pk)
    form = KeyForm(instance=key)

    if request.method == 'POST':
        form = KeyForm(request.POST, instance=key)
        if form.is_valid():
            form.save()
            return redirect('/keys/')

    context = {'form': form}
    return render(request, 'organization/create_entity.html', context)

