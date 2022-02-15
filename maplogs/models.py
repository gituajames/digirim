from django.db import models
# from django.db.models.fields.files import ImageField
from django.urls import reverse
from PIL import Image


class Map(models.Model):
    map_category_choices = [
        ('Cadastral', 'cadastral map'),
        ('General Boundary', 'general boundary'),
        ('PDP', 'pdp')
    ]

    county_choices = [
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Nyeri', 'Nyeri'),
        ('Nyandarua', 'Nyandarua'),
    ]

    title = models.CharField(max_length=200)
    scanned = models.BooleanField()
    upload_date = models.DateField(auto_now=True)
    stamped_county_date = models.DateField(auto_now=False, auto_now_add=False)
    county = models.CharField(max_length=50, choices=county_choices, default='Nyandarua')
    map_category = models.CharField(max_length=100, choices=map_category_choices, default='General Boundary')
    image = models.ImageField(upload_to='maps/%Y/%m/%d', blank=True)
    # thumbnail = models.ImageField(upload_to='maps/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('-stamped_county_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('maps:map_details', args=[self.id])

    def get_thumbnail(self):
        if self.thumbnail:
            return reverse('maps:map_detail, ')
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail
            else:
                return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        img.save('JPEG', quality=85)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('maps:product_detail', args=[self.id, self.slug])


''' 
1. create a new advanced search
2. how to handle redundant maps

'''
