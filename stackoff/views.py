from django.shortcuts import render,HttpResponse
from .models import QuestionModel
from rest_framework import viewsets
from .serializers import QuestionSerializer
import urllib3
from .forms import SubmitForm
import json
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone

# Create your views here.
class QuestionApi(viewsets.ModelViewSet):
    queryset=QuestionModel.objects.all()
    serializer_class=QuestionSerializer
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    

    return int(h) * 3600 + int(m) * 60 + float(s)



# def question_form(request):
#   form=SubmitForm()
#   if request.method=="POST":
#       form=SubmitForm(request.POST)
#       query=request.POST.get('query')
#       objects=QuestionModel.objects.all()
#       for i in objects:
#           if i.query==query:
#              queryset=objects.filter(query=query)
#              page=request.GET.get('page')
#              paginator=Paginator(queryset,10)
#              pag=paginator.page(1)
#              return render(request,'stackoff/questions.html',{'page_obj':pag})

#       http=urllib3.PoolManager()
#       r= http.request('GET',query)
#       data=json.loads(r.data.decode('utf-8')) 
#       for i in range(len(data['items'])):
#           quest=QuestionModel()
#           quest.query=query
#           quest.link=data['items'][i]['link'];
#           quest.title=data['items'][i]['title']
#           quest.save()
            
#       queryset=QuestionModel.objects.all().filter(query=query)
#       page=request.GET.get('page')
#       paginator=Paginator(queryset,10)
#       pag=paginator.page(1)

#       return render(request,'stackoff/questions.html',{'page_obj':pag})
            
#   return render(request,'stackoff/home.html',{'form':form})


def quest_form_test(request):
    if  request.GET.get('query'):
        request.session['query']=request.GET.get('query')
        query=request.GET.get('query')
        print("not None")
    else:
        query=request.session.get('query')
        print('none')


    try:

       request.session['count']+=1


       
       

    except:
       request.session['count']=1
       
       request.session['time']=get_sec(timezone.now().time().isoformat())


    try:
        request.session['day_count']+=1
   
    except:
        request.session['day_count']=1
        request.session['day_time']=get_sec(timezone.now().time().isoformat())



    if request.session['count']>5 and (get_sec(timezone.now().time().isoformat())-request.session['time'])<60:
        request.session['time']=get_sec(timezone.now().time().isoformat())
        


        return render(request,'stackoff/error.html',{})

    if request.session['day_count']>100 and (get_sec(timezone.now().time().isoformat())-request.session['day_time'])<86400:
        request.session['day_time']=get_sec(timezone.now().time().isoformat())
        return render(request,'stackoff/error.html',{})


    if (get_sec(timezone.now().time().isoformat())-request.session['time'])>60:
        request.session['count']=0


    if (get_sec(timezone.now().time().isoformat())-request.session['day_time'])>86400:
        request.session['day_count']=0 






    objects=QuestionModel.objects.all().order_by('title')
    for i in objects:
        if i.query==query:
                   queryset=objects.filter(query=query)
                   page = request.GET.get('page', 1)
                   
                   paginator = Paginator(queryset, 10)
                   try:
                      pag = paginator.page(page)
                   except PageNotAnInteger:
                      pag = paginator.page(1)
                   except EmptyPage:
                      pag = paginator.page(paginator.num_pages)

                   return render(request,'stackoff/questions.html',{'page_obj':pag})

    http=urllib3.PoolManager()
    r= http.request('GET',query)
    data=json.loads(r.data.decode('utf-8')) 
    if  not  data['items']:
        return render(request,'stackoff/notfound.html',{})
    
    for i in range(len(data['items'])):
        quest=QuestionModel()
        quest.query=query
        quest.link=data['items'][i]['link'];
        quest.title=data['items'][i]['title']
        quest.save()
        
    queryset=QuestionModel.objects.all().filter(query=query)
    page=request.GET.get('page')
    
    paginator=Paginator(queryset,10)

    try:
       pag = paginator.page(page)
    except PageNotAnInteger:
       pag = paginator.page(1)
    except EmptyPage:
       pag = paginator.page(paginator.num_pages)
   

    return render(request,'stackoff/questions.html',{'page_obj':pag})
            
    





def initial_page(request):
    form=SubmitForm()
    return render(request,'stackoff/home.html',{'form':form})
