import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit


this_dir =  pathlib.Path(__file__).resolve().parent



def home_page_view(request, *args, **kwargs):
    
    qs = PageVisit.objects.all()
    my_page = 'My page' 
    page_qs = PageVisit.objects.filter(path=request.path)
    my_context = {
        'page_title':my_page,
        'page_visit_count':page_qs.count(),
        'tota_visite_count': qs.count(),
        'percent': page_qs.count() * 100/ qs.count()        
        }
    PageVisit.objects.create(path=request.path)
    return render(request, 'home.html', my_context)

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