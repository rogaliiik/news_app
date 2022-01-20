from django.shortcuts import render
from app_media.forms import *
from django.http import HttpResponse


def upload_file(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            file = request.FILES['file']
            return HttpResponse(content=(file.name + ' ', file.size/1000000, ' Мбайт'), status=200)
    else:
        upload_file_form = UploadFileForm()
    context = {
        'form':upload_file_form
    }
    return render(request, 'upload_file.html', context=context)
