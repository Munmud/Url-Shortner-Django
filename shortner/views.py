from django.shortcuts import render, redirect
import uuid
from .models import Url
import validators


# Create your views here.
def index(request):
    print('index')
    if request.method=='POST' :
        url = request.POST['link']

        if not validators.url(url):
            return redirect('index')
        
        url_details = None
        uid = str(uuid.uuid4())[:5]
        
        for i in range(1000) :
            url_details = Url.objects.filter(uuid = uid).first()
            if url_details == None :
                break
            uid = str(uuid.uuid4())[:5]
        
        if url_details != None :
            return render(request, 'index.html')

        
        newUrl = Url(link = url,uuid = uid)
        newUrl.save()
        return redirect('res/'+ str(uid))

    return render(request, 'index.html')

def go(request , pk):
    print('go' , pk)
    url_details = Url.objects.filter(uuid = pk).first()
    if url_details == None :
        return redirect('index')
    return redirect(url_details.link)

def res(request , pk):
    print('res' , pk)
    return render(request, 'result.html', {'pk' : pk , })
