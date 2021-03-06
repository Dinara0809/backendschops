from django.db import models
from authentication.models import User
from products.models import Product


class CartManger(models.Manager):
    def get_or_new(self, request):
        user = request.user
        cart_id = request.session.get('cart_id', None)
        if user is not None and user.is_authenticated:
            if user.cart:
                cart_obj = request.user.cart
            else:
                cart_obj = Cart.objects.get(pk=cart_id)
                cart_obj.user = user
                cart_obj.save()
            return cart_obj
        else:
            cart_obj = Cart.objects.get_or_create(pk=cart_id)
            cart_id = request.session['cart_id'] = cart_obj[0].id
            return cart_obj[0]


class Cart(models.Model):
    user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
    objects = CartManger()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_in_cart')
    amount = models.PositiveIntegerField(default=1, blank=True)


