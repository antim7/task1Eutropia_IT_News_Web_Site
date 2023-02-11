from django.shortcuts import render
from django.shortcuts import render, HttpResponse,redirect
from myproject.forms import NewsForm
from myproject.models import Createnews

# Create your views here.
def news(request):
    news_list = Createnews.objects.all()
    return render(request, 'news.html', {'news_list': news_list})

def createnewspage(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        #context={'form':form}
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = NewsForm()
        context = {'NewsForm': form}
    return render(request, 'news.html', context)


def deletenewspage(request):

    return render(request,'deletenews.html')

def updatenewspage(request):

    return render(request,'updatenews.html')