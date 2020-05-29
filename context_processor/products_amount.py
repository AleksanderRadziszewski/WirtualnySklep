from WirtualnyOptyk.models import CartProducts


def amount(request):
     amount=sum([product.quantity for product in CartProducts.objects.all()])
     products_amount={
         "prod_amount":amount
     }
     return products_amount