from django.shortcuts import render
from django.http import HttpResponse
from .models import Design_object, Spot, Task, Department, Employee, UploadFiles
from .forms import AddPostForm, UploadFileForm
from .serializers import TaskSerializer, DesignobjectSerializer, SpotSerializer, DepartmentSerializer, EmployeeSerializer
from rest_framework import generics



# Авторизованные пользователи

class TaskAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DesignobjectAPIView(generics.ListAPIView):
    queryset = Design_object.objects.all()
    serializer_class = DesignobjectSerializer

class SpotAPIView(generics.ListAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class DepartmentAPIView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Админ



class TaskAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DesignobjectAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Design_object.objects.all()
    serializer_class = DesignobjectSerializer

class SpotAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Spot.objects.all()
    serializer_class = SpotSerializer

class DepartmentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer









def task(request): 
    objs = Design_object.objects.all()
    spots = Spot.objects.all()
    tasks = Task.objects.all()
    form = AddPostForm()
    data = {'titles':'All objects',
            'objs': objs,
            'spots': spots,
            'tasks': tasks,
            'form1':form}
    return render(request, 'main.html', context=data)


# def addpage(request):
#     return render(request, 'main.html')


def index(request):
    # print(request)
    # print(request.scheme)   
    # print(request.path)
    # print(request.encoding) 
    return HttpResponse('<h1>Hello word!</h1>')

def about(request):
    return HttpResponse('<a href="#"> About page!</a>')




def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
        #    handle_uploaded_file(form.cleaned_data['file'])
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
 
    return render(request, 'uploads.html', {'form': form})