from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse


articles = {
    'sport':'Sports Page',
    'finance':'Finance Page',
    'politics':'Politics Page',
}

def simple_view(request):
    return render(request,'first_app/example.html')

def news(request,topic):
   try:
       result = articles[topic]
       return HttpResponse(articles[topic])
   except:
      raise Http404('404 Default')
       
  
def add_value(request, num1, num2):
    jumlah = num1 + num1
    return HttpResponse(str(jumlah))


def num_page_view(request,num_page):
    topic_list = list(articles.keys())
    topic = topic_list[num_page]
    wepage = reverse('topic-page',args=[topic])
    return HttpResponseRedirect(wepage)

def example_view(request):
    return render(request,"first_app/wow.html")


def variable_view(request):
    my_var = {
        'first_name' :'arseno',
        'last_name' : ' Alzahabi',
        'list' : [1,2,3],
        'dictonary' : {'inside_key':'inside_value'},
        'user_logged_in' : False
    }
    return render(request,'first_app/variable.html',my_var)
    

