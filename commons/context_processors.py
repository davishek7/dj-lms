from courses.models import Category
from courses.forms import SearchForm


def global_context(request):
    
    return{
        'categories' : Category.objects.all(),
        'search_form' : SearchForm()
    }