from django.shortcuts import render, HttpResponse

contenido_html = """
<h1>Menú navegación</h1>
<ul>
    <li><a href="/">Índice</a></li>
    <li><a href="/about/">Sobre mí</a></li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')


