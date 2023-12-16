from collections.abc import Iterable
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Village = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20, unique=True, blank=False)
    Gmail = models.EmailField(unique=True, blank=True)
    profilephoto = models.ImageField(
        upload_to="images/profilephotos", default="")
    created_at = models.DateTimeField(default="", editable=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        return super().save(*args, **kwargs)


@receiver(pre_delete, sender=Customers)
def delete_profile_photo(sender, instance, *args, **kwargs):
    if instance.profilephoto:
        storage, path = instance.profilephoto.storage, instance.profilephoto.path
        if storage and path and storage.exists(path):
            storage.delete(path)


class Measurements(models.Model):
    customer = models.OneToOneField(
        Customers, on_delete=models.CASCADE, primary_key=True)
    Neck = models.FloatField(null=True, blank=True)
    Chest = models.FloatField(null=True, blank=True)
    Waist = models.FloatField(null=True, blank=True)
    Hips = models.FloatField(null=True, blank=True)
    Thigh = models.FloatField(null=True, blank=True)
    Knee = models.FloatField(null=True, blank=True)
    Calf = models.FloatField(null=True, blank=True)
    Sleeve = models.FloatField(null=True, blank=True)
    Back = models.FloatField(null=True, blank=True)
    Waistband = models.FloatField(null=True, blank=True)
    Outseam = models.FloatField(null=True, blank=True)
    Inseam = models.FloatField(null=True, blank=True)
    Ankle = models.FloatField(null=True, blank=True)


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=30)
    garment_drop_off = models.DateField()
    requested_pick_up_date = models.DateField()
    price = models.IntegerField(default=0)
    garment_pick_up = models.DateField(null=True, blank=True)
    clothimage = models.ImageField(upload_to="images/clothimages", default="")
    design = models.ImageField(upload_to="images/design", default="")
    is_stitched = models.BooleanField(default=False)


@receiver(pre_delete, sender=Products)
def delete_products_image(sender, instance, **kwargs):
    if instance.clothimage:
        storage, path = instance.clothimage.storage, instance.clothimage.path
        if storage and path and storage.exists(path):
            storage.delete(path)
    if instance.design:
        storage, path = instance.design.storage, instance.design.path
        if storage and path and storage.exists(path):
            storage.delete(path)


class Transactions(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_date = models.DateField()
    total_amount = models.IntegerField()
    advance_amount = models.IntegerField()

    @property
    def due_amount(self):
        return self.total_amount - self.advance_amount
