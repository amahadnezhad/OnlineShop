
class Cart:
    def __init__(self, request):
        """
        Initialize The Cart
        """
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}
            # cart = self.session['cart']

        self.cart = cart

    def add(self, product, quantity=1):
        """
        Add The Specified Product To The Cart If It Exists
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity}

        else:
            self.cart[product_id][quantity] += quantity

        self.save()

    def remove(self, product):
        """
        Remove a Product From The Cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        Mark Session As Modified To Save Changes
        """
        self.session.modified = True
