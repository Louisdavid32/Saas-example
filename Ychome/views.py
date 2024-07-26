import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


this_dir =  pathlib.Path(__file__).resolve().parent



def home_page_view(request, *args, **kwargs):
    
    return about_view(request, *args, **kwargs)

def home_old_page_view(request):
    print(this_dir)
    html_="""    <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <h1>hello is youncoder </h1>
            </body>
            </html>"""
            
    html_file_pht = this_dir/'home.html'
    html_ = html_file_pht.read_text()
    return HttpResponse(html_)

def about_view(request , *args, **kwargs):
    my_page = 'My page' 
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = page_qs.count() * 100/ qs.count()
    except:
        percent=0
        
    my_context = {
        'page_title':my_page,
        'page_visit_count':page_qs.count(),
        'tota_visite_count': qs.count(),
        'percent':percent         
        }
    
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', my_context)
