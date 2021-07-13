from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})
    else:
        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})