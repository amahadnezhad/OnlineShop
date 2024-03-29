from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404, reverse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Product, Comment
from .forms import CommentForm
from cart.forms import AddToCartProductForm


def test_translation(request):
    result = _('Hello')
    messages.error(request, "This is success message")
    return render(request, "products/test_hello.html")


class ProductListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['add_to_cart_form'] = AddToCartProductForm()
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('product_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        obj.product = product

        messages.success(self.request, _("Comment Successfully Created!"))

        return super().form_valid(form)
