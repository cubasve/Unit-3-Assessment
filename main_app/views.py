from django.shortcuts import render, redirect
# from django.views.generic.edit import DeleteView
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum  #for bonus


def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    total = Widget.objects.aggregate(sum=Sum('quantity'))['sum']
    return render(request, 'index.html', {
        'widgets': widgets,
        'widget_form': widget_form,
        'total': total,
    })


def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        create_widget = form.save(commit=False)
        create_widget.save()
    return redirect('/')


def delete_widget(request, widget_id):
    Widget.objects.get(id=widget_id).delete()
    return redirect('/')


# class WidgetDelete(DeleteView):
#     model = Widget
#     fields = ['description', 'quantity']
#     success_url = '/'
