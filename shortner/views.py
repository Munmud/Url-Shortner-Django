from django.shortcuts import render, redirect, get_object_or_404
import uuid
import validators
from django.utils import timezone

from .models import Url
from .forms import UrlForm


from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    print('index')
    if request.method == 'POST':
        url = request.POST['link']

        if not validators.url(url):
            return redirect('index')

        url_details = None
        uid = str(uuid.uuid4())[:5]

        for i in range(1000):
            url_details = Url.objects.filter(uuid=uid).first()
            if url_details == None:
                break
            uid = str(uuid.uuid4())[:5]

        if url_details != None:
            return render(request, 'index.html')

        newUrl = Url(link=url, uuid=uid, user=request.user)
        newUrl.save()
        return redirect('res/' + str(uid))

    urls = Url.objects.filter(user=request.user).all()
    return render(request, 'index.html', {'urls': urls})


def go(request, pk):
    print('go', pk)
    url_details = Url.objects.filter(uuid=pk).first()
    if url_details == None:
        return redirect('index')

    if timezone.now() > url_details.expire_date:
        return redirect('index')

    url_details.visit_count += 1
    url_details.save()
    return redirect(url_details.link)


def res(request, pk):
    print('res', pk)
    return render(request, 'result.html', {'pk': pk, })


def url_edit(request, uuid):
    url = get_object_or_404(Url, uuid=uuid)
    if request.method == 'POST':
        form = UrlForm(request.POST, instance=url)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UrlForm(instance=url)
    return render(request, 'url_edit.html', {'form': form, 'url': url})


def url_delete(request, uuid):
    url = get_object_or_404(Url, uuid=uuid)
    if request.method == 'POST':
        url.delete()
        return redirect('index')
    return render(request, 'url_confirm_delete.html', {'url': url})
