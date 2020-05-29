from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.signals import user_logged_in
import datetime

def create_profile(sender, user, request, **kwargs):
    Profile.objects.get_or_create(user=user)

user_logged_in.connect(create_profile)


plastic = 1
metal = 2
siluetts = 3

frames = (
    (plastic, "plastic_frames"),
    (metal, "metal_frames"),
    (siluetts, "siluetts"))

one_day = 1
repeated_use = 2
one_year = 3

contact_lenses = (
    (one_day, "one day"),
    (repeated_use, "repeated use"),
    (one_year, "one year"))

corrective = 1
progressive = 2
photochromes = 3
shaded = 4

large_glass_cleaner = 1
small_glass_cleaner = 2
lens_liquid = 3
eyeglass_chains = 4
eyeglass_cloth = 5

glasses = (
    (corrective, "corrective"),
    (progressive, "progressive"),
    (photochromes, "photochromes"),
    (shaded, "shaded"))

accessories = (
    (large_glass_cleaner, "Big glass cleaner"),
    (small_glass_cleaner, "small glass cleaner"),
    (lens_liquid, "lens liquid"),
    (eyeglass_chains, "eyeglass chains"),
    (eyeglass_cloth, "eyeglass cloth"))


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    foto = models.ImageField(upload_to='static/list_photos', height_field=None, width_field=None, max_length=100,
                             null=True,
                             verbose_name="Photo:")
    available = models.BooleanField(default=True, verbose_name="Avaiable:")

    def get_type(self):

        if hasattr(self, 'frames'):
            return self.frames.get_type_display()
        if hasattr(self, 'glasses'):
            return self.glasses.get_type_display()
        if hasattr(self, 'accessories'):
            return self.accessories.get_type_display()
        if hasattr(self, 'contactlenses'):
            return self.contactlenses.get_type_display()

    def __str__(self):
        return self.name


class Frames(Product):
    type = models.IntegerField(choices=frames)

    def get_update_url(self):
        return f"/frame_update/{self.id}/"

    def get_detail_url(self):
        return f"/frame_detail/{self.id}/"

    def get_delete_url(self):
        return f"/delete_frame/{self.id}/"

    def __str__(self):
        return self.name


class Accessories(Product):
    type = models.IntegerField(choices=accessories)

    def get_update_url(self):
        return f"/accessories_update/{self.id}/"

    def get_detail_url(self):
        return f"/accessories_detail/{self.id}/"

    def get_delete_url(self):
        return f"/accessories_delete/{self.id}/"

    def __str__(self):
        return self.name


class ContactLenses(Product):
    type = models.IntegerField(choices=contact_lenses)

    def get_update_url(self):
        return f"/contact_lenses_update/{self.id}/"

    def get_detail_url(self):
        return f"/contact_lenses_detail/{self.id}/"

    def get_delete_url(self):
        return f"/contact_lenses__delete/{self.id}/"

    def __str__(self):
        return self.name


class Glasses(Product):
    type = models.IntegerField(choices=glasses)

    def get_update_url(self):
        return f"/glasses_update/{self.id}/"

    def get_detail_url(self):
        return f"/glasses_detail/{self.id}/"

    def get_delete_url(self):
        return f"/glasses_delete/{self.id}/"

    def __str__(self):
        return self.name


class Profile(models.Model):
    phone_number = models.CharField(max_length=40)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.TextField()


class Supply(models.Model):
    provider = models.CharField(max_length=40)
    delivery_time = models.IntegerField()
    delivery_price = models.FloatField()

    def __str__(self):
        return f"{self.provider}-{self.delivery_time} days - {self.delivery_price} zł"


class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartProducts")



class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.quantity == 0:
            self.delete()
        else:
            super().save(force_insert, force_update, using, update_fields)



class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,through="OrderProduct")
    provider = models.ForeignKey(Supply, on_delete=models.CASCADE)
    date_of_order=models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return str(self.id)


class OrderProduct(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
# Create your models here.
