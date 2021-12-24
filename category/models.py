from django.db import models

# Create your models here.
class Category(models.Model): # we use PascalCase
    #1.Property
    cat_name = models.CharField(max_length=50)
    cat_slug = models.SlugField(max_length=255)
    cat_desc = models.TextField(max_length=255)
    cat_image = models.ImageField(upload_to='uploads/categories')

    #2 Constructor

    #3. Method
    def __str__(self):
        return self.cat_name

    #4. Nested Class
    class Meta:
        #1. Property
        verbose_name = 'category' # singlular form
        verbose_name_plural = 'categories' # plural form
        #2. Constructor
        #3. Method
        #4. Nested Class
        pass
    
