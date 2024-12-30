from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   return render (request ,'index.html')

def Remove(request):
    djtext=request.GET.get('text','default')
    remove= request.GET.get('remove','off')
    print(remove)
    print(djtext)
    # analyzed= djtext
    if remove == "on":
        punctuations= '''!()-[]{};:'"\,<>/.?@#$%&*'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+ char
        par ={ 'purpose':'Remove punctuations ', 'analyze_text': analyzed}
        return render(request, 'remove.html', par)
    else:
        return HttpResponse("Plz  click on Checkbox <a href='/'>Back</a>")

def capfirst(request):
    return HttpResponse("Capitalized first")

def newlineremove(request):
    return HttpResponse("New line remove")