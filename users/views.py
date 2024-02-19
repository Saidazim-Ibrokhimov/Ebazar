from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, UpdateProfileForm
from django.views import View
from django.contrib import messages
from .models import CustomeUser, Saved
from products.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class SignUpView(UserPassesTestMixin, View):
    def get(self, request):
        return render(request, 'registration/signup.html', {'form':SignUpForm()})
    
    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are signed in!')
            return redirect('login')

        return render(request, 'registration/signup.html', {'form':SignUpForm()})
    
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            return False
        return True
    
class ProfileView(View):
    def get(self, request, username):
        user = get_object_or_404(CustomeUser, username=username)

        return render(request, 'profile.html', {'user':user})
    
class UpdateProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = UpdateProfileForm(instance=request.user)
        return render(request, 'profile_update.html', {'form':form})
    
    def post(self, request):
        form = UpdateProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have updated your profile!')
            return redirect('users:profile', request.user.username)
        
        return render(request, 'profile_update.html', {'form':form})



class AddRemoveSavedView(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        saved_product = Saved.objects.filter(user=request.user, product=product)

        if saved_product:
            saved_product.delete()
            messages.info(request, 'Removed')
        else:
            Saved.objects.create(user=request.user, product=product)
            messages.info(request, 'Saved')
        return redirect(request.META.get("HTTP_REFERER"))
    
class SavedView(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        saveds = Saved.objects.filter(user=request.user)
        return render(request, 'saveds.html', {'saveds':saveds})
    
class RecentlyViewedView(View):
    def get(self, request):
        context = {}
        if not 'recently_viewed' in request.session:
            products = []
        else:
            r_viewed = request.session['recently_viewed']
            products = Product.objects.filter(id__in=r_viewed)
            context['products'] = products

            if request.user.is_authenticated:
                saveds = Saved.objects.filter(user=request.user)
                saved_products = [saved.product for saved in saveds]

                context['saved_products'] = saved_products
       
        return render(request, 'recently_viewed.html', context)


        
