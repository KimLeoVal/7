#
# from django.shortcuts import get_object_or_404, redirect
# from django.urls import reverse, reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
#
# from webapp.forms import PollForm, ChoiceForm
# from webapp.models import Poll, Choice, Answer
#
#
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm, ReviewForm
from webapp.models import Product, Review


class ProductsView(ListView):
    model = Product
    template_name = 'for_product/index.html'
    context_object_name = 'products'
    paginate_by = 5



    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        products=[]
        object_list=Product.objects.all()
        for product in object_list:
            total = 0
            review = product.review.filter(mod=1)
            for i in review:
                total+=i.score
            avg = total/len(review)
            product.avg = avg
            products.append(product)
        context['products']=products
        return context

#
class ProductDetaillView(DetailView):
    model = Product
    template_name = 'for_product/view.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        total = 0
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        review = product.review.filter(mod=1)
        for i in review:
            total+=i.score
        avg = total/len(review)
        context['avg']=avg
        return context




class ProductCreate(PermissionRequiredMixin,CreateView):
    template_name = 'for_product/create.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self):
        return reverse('webapp:ProductDetaillView', kwargs={'pk': self.object.pk})
#
class ProductUpdate(PermissionRequiredMixin,UpdateView):
    template_name = 'for_product/update.html'
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.change_product'



    def get_success_url(self):
        return reverse('webapp:ProductDetaillView', kwargs={'pk': self.object.pk})
#
class ProductDelete(PermissionRequiredMixin,DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'for_product/delete.html'
    success_url = reverse_lazy('webapp:ProductsView')
    permission_required = 'webapp.delete_product'
#


class ReviewView(ListView):
    model = Review
    template_name = 'for_review/view.html'
    context_object_name = 'review'





class ReviewDetaillView(DetailView):
    model = Review
    template_name = 'for_review/detailview.html'
    context_object_name = 'review'





class ReviewCreate(CreateView):
    template_name = 'for_review/create.html'
    form_class = ReviewForm


    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:ReviewDetaillView', kwargs={'pk': self.object.pk})
#
class ReviewUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'for_review/update.html'
    model = Review
    form_class = ReviewForm
    permission_required = 'webapp.change_review'

    def has_permission(self):
        return super().has_permission() and self.request.user == self.get_object().review.author

    def form_valid(self, form):
        if  self.request.user.is_superuser:
            self.object = form.save()
        else:
            self.object = form.save()
            self.object.mod = False
            self.object.save()
        return super().form_valid(form)




    def get_success_url(self):
        return reverse('webapp:ReviewDetaillView', kwargs={'pk': self.object.pk})
#
class DeleteReview(PermissionRequiredMixin, DeleteView):
    model = Review
    context_object_name = 'review'
    template_name = 'for_review/delete.html'
    success_url = reverse_lazy('webapp:ReviewView')
    permission_required = 'webapp.delete_review'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().review.author.all()
#
#

#
#
#
#
#
#
#
