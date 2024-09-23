from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)  # Name of the category
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)  # Optional description
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        """
        Returns the URL to access products in this category.

        Parameters:
        self (Category): The instance of the Category model.

        Returns:
        str: The URL to access products by category.
        """
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        Returns the string representation of the Category instance.

        Parameters:
        self (Category): The instance of the Category model.

        Returns:
        str: The string representation of the category name.

        This method is used to display the category name in Django's admin interface 
        and other places where the Category instance needs to be represented as a string.
        """
        return self.category_name
