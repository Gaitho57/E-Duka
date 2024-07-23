from .models import Category

def menu_links(request):
    """
    This function retrieves all categories from the database and returns them as a dictionary.

    Parameters:
    request (HttpRequest): The incoming request object.

    Returns:
    dict: A dictionary containing the retrieved categories. The dictionary has a single key-value pair, where the key is 'links' and the value is a QuerySet of Category objects.
    """
    links = Category.objects.all()
    return dict(links=links)