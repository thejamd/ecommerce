from store.models import Products
class Cart():
    def __init__(self,request):
        self.session  = request.session
        
        #get the current session if it exist
        cart = self.session.get('session_key')
        
        #if the user is new no session key create new key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        #make sure session key available on all the pages
        self.cart =cart
        
    def add(self,product,quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id]={'price':str(product.price)}
            self.cart[product_id]=int(product_qty )
        self.session.modified = True
    def __len__(self):
        return len(self.cart)
    def get_prods(self):
        #get ids from the cart
        product_ids = self.cart.keys()
        #use ids to lookup products in the db
        products = Products.objects.filter(id__in =product_ids)
        return products
    def get_quants(self):
        quantities = self.cart
        return quantities
    def update(self,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        our_cart = self.cart
        our_cart[product_id]= product_qty
        self.session.modified = True
        thing = self.cart
        return thing
    def delete(self,product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        self.session.modified = True