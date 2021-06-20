from .models import Category
from .forms import SearchForm


def categories(request):
    
    return{
        'categories' : Category.objects.all()
    }

def search_form(request):

    return{
        'search_form' : SearchForm()
    }