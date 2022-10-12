from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    txt = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        para = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        txt = analyzed

    if(uppercase=="on"):
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()

        para = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        txt = analyzed

    if(lowercase == "on"):
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.lower()

        para = {'purpose': 'Changed to LowerCase', 'analyzed_text': analyzed}
        txt = analyzed

    if(extraspaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(txt):
            if not(txt[index] == " " and txt[index+1] == " "):
                analyzed = analyzed + char

        para = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        txt = analyzed

    if (newlineremove == "on"):
        analyzed = ""
        for char in txt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        para = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        txt = analyzed

    if(removepunc != "on" and uppercase != "on" and lowercase != "on" and newlineremove != "on" and extraspaceremove != "on"):
        return HttpResponse("<h4 align:'center'>Please Enter Any Utils</h4>")

    return render(request, 'analyze.html', para)
