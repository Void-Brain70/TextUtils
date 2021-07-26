from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Welcome to Void Brain</h1><a href="https://dasanik70.blogspot.com/">Void Brain</a>''')

def index(request):
    return render(request,"index.html")

def analyze(request):
    # Get the text
    t = request.GET.get('text','default')
    # check checkbox
    r = request.GET.get('removepunc','off')
    f = request.GET.get('fullcaps','off')
    n = request.GET.get('newlineremover','off')
    s = request.GET.get('spaceremover','off')
    w = request.GET.get('wordcounter','off')
    
    if r == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in t:
          if char not in punctuations:
            analyzed = analyzed + char
        dic={
           'purpose': 'Removed Punctutions',
           'analyze_txt': analyzed
        }
        return render(request,"analyze.html",dic)
    
    elif(f=='on'):
        analyzed = " "
        for char in t:
            analyzed = analyzed + char.upper()
        dic={
           'purpose': 'Changed to Uppercase',
           'analyze_txt': analyzed
        }    
        return render(request,"analyze.html",dic)
    
    elif(n=='on'):
        analyzed = " "
        for char in t:
            if char !='\n':
                analyzed = analyzed + char
        dic={
           'purpose': 'Remove Space',
           'analyze_txt': analyzed
        }    
        return render(request,"analyze.html",dic)
    
    elif(s=='on'):
        analyzed = " "
        for index,char in enumerate(t):
            if t[index] ==' ' and t[index+1]==' ':
                pass
            else:
                analyzed = analyzed + char
        dic={
           'purpose': 'Remove Space',
           'analyze_txt': analyzed
        }    
        return render(request,"analyze.html",dic)
    
    elif(w=='on'):
        analyzed = 0
        for char in t.split():
           analyzed = analyzed +1
        dic={
           'purpose': 'Total Word is',
           'analyze_txt': analyzed
        }    
        return render(request,"analyze.html",dic)                   
    
    else:
        return HttpResponse("<h1>Error</h1>")     
     