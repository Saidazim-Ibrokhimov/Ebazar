from django.shortcuts import render, get_object_or_404
from django.views import View
from products.models import Product, Category
from users.models import Saved

# Create your views here.

def for_all_pages(request):
      categories = Category.objects.all()

      return {'categories':categories}


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        q = request.GET.get('q', '')
        if q:
            products = products.filter(title__icontains=q)

        context =  {
            'products':products,
            'q':q
            }

        if request.user.is_authenticated:
            saveds = Saved.objects.filter(user=request.user)
            saved_products = [saved.product for saved in saveds]

            context['saved_products'] = saved_products
       



        return render(request, 'index.html', context)
    
class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(category=category)


        return render(request, 'category.html', {'products':products, 'category':category})

