from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.
    
    # Renderiza la plantilla HTML /catalog/templates/index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors},
    )

def booklist(request):
    """
    Función vista para la lista de libros
    """
    # Genera contadores de algunos de los objetos principales
    books=Book.objects.all()
    
    # Renderiza la plantilla HTML /catalog/templates/index.html con los datos en la variable contexto
    return render(
        request,
        'book_list.html',
        context={'books':books},
    )

def authorlist(request):
    """
    Función vista para la lista de libros
    """
    # Genera contadores de algunos de los objetos principales
    authors=Author.objects.all()
    
    # Renderiza la plantilla HTML /catalog/templates/index.html con los datos en la variable contexto
    return render(
        request,
        'author_list.html',
        context={'authors':authors},
    )


def bookdetailview(request,id):
    try:
        book_id=Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'book_detail.html',
        context={'book':book_id},
    )

def authordetailview(request,id):
    try:
        author_id=Author.objects.get(id=id)
    except Author.DoesNotExist:
        raise Http404("Author does not exist")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'author_detail.html',
        context={'author':author_id},
    )