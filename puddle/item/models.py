from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories' # It will give us Categories in admin pannel.
        
    def __str__(self):
        return self.name # It will show the category object name.

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE) # if category is deleted then all items belong to this also be deleted.
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True) #if item_images doesn't exist then django make it.
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE) # This is an index into database b/w this item and user. # Cascade means if user is deleted then all of the items are also deleted.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name # It will show the category object name.
