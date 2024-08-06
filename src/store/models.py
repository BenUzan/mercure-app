from django.db import models

# Create your models here.


class Store(models.Model):
    name = models.CharField(max_length=50)
    localistation = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)  # ! La taille A revoir !!!
    product_code = models.CharField(max_length=100)  # ! La taille a revoir !!!
    price_achat = models.DecimalField(max_digits=18, decimal_places=2)
    price_revient = models.DecimalField(max_digits=18, decimal_places=2)
    marge = models.DecimalField(max_digits=18, decimal_places=2)
    price_ventes = models.DecimalField(max_digits=18, decimal_places=2)
    benefice = models.DecimalField(max_digits=18, decimal_places=2)


class StockProduct(models.Model):
    fk_product_code = models.CharField(max_length=10)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=10)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=18, decimal_places=2)


class InvoiceItems(models.Model):
    # invoice = models.ForeignKey(
    #     "store.Invoice", on_delete=models.CASCADE, default=True)
    date = models.DateTimeField(auto_now_add=True)  # ! Remove after
    quantity = models.IntegerField()
    unity_price = models.DecimalField(max_digits=18, decimal_places=2)
    total_price = models.DecimalField(max_digits=18, decimal_places=2)
    discount = models.DecimalField(max_digits=18, decimal_places=2)
    total_profit = models.DecimalField(max_digits=18, decimal_places=2)


class Report(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    # user_id = models.ForeignKey(
    #  "store.Model", verbose_name=(""), on_delete=models.CASCADE)
