from django.shortcuts import render, redirect, get_object_or_404
from .forms import bangdata
import base64
from django.core.files.base import ContentFile
from .models import data



def formdata(request):
    if request.method == 'POST':
        form_data = bangdata(request.POST, request.FILES)
        
        if form_data.is_valid():
            print("📦 POST data:", request.POST)
            print("📂 FILES data:", request.FILES)
            nuevo_data = form_data.save(commit=False)
            
           
            firma_base64 = request.POST.get('firma_base64')
            if firma_base64:
                print("📦 POST data:", request.POST)
                print("📂 FILES data:", request.FILES)
                formato, imgstr = firma_base64.split(';base64,') 
                ext = formato.split('/')[-1]
                data_firma = ContentFile(base64.b64decode(imgstr), name=f'firma.{ext}')
                nuevo_data.firma = data_firma  

        
            nuevo_data.save()
            return redirect('index')
    else:
        
        form_data = bangdata()

    return render(request, 'supdata/formdata.html', {
        'form_data': form_data,
    })

def viewtable(request):
    datos = data.objects.all()   
    
    return render(request, 'supdata/records.html',{'datos':datos})


def reports(request,id):

    report = get_object_or_404(data, pk=id)
    
    
    return render(request, 'supdata/report.html',{'report':report})