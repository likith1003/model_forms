from django.shortcuts import render,HttpResponse
from app.forms import *
# Create your views here.
def create_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        TFDO.save()
        return HttpResponse('Topic Created Successfully')
    return render(request, 'create_topic.html',d)

def create_webpage(request):
    return render(request, 'create_webpage.html')