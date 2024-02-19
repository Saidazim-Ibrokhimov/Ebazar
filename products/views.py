from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, UpdateProductForm
from .models import ProductImage, Product, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def new_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_new.html', {'form':form})
    
    elif request.method == "POST":
        form = ProductForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save(request)
            for image in request.FILES.getlist('images'):
                ProductImage.objects.create(image=image, product=product)
            messages.success(request, 'You have succesfully created new product!')
            return redirect('products:detail', product.id)
        
        return render(request, 'product_new.html', {'form':form})
    
def productDetail(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, id=id)

        if "recently_viewed" in request.session:
            r_viewed = request.session['recently_viewed']
            if not product.id in r_viewed:
                r_viewed.append(product.id)
                request.session.modified = True
        else:
            request.session['recently_viewed'] = [product.id]
        print(request.session['recently_viewed'])
        return render(request, 'product_detail.html', {'product':product})
    
@login_required(login_url='login')  
def updateProduct(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user == product.author:
        if request.method == 'GET':
            form = UpdateProductForm(instance=product)
            return render(request, 'update_product.html', {'form':form, 'product':product})
        
        elif request.method == "POST":
            form = ProductForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                product = form.save(request)
                if request.FILES.getlist('images',):
                    ProductImage.objects.filter(product=product).delete()
                    for image in request.FILES.getlist('images'):
                        ProductImage.objects.create(image=image, product=product)
                messages.success(request, 'You have update product details!')
                return redirect('products:detail', product.id)
            
            return render(request, 'product_new.html', {'form':form})
    else:
        messages.warning(request, "You cannot edit the product details")
        return redirect('products:detail', product.id)
@login_required(login_url='login')
def deleteProduct(request, id):
    product = get_object_or_404(Product, id=id)
    if request.user == product.author:
        if request.method == 'POST':
            product.delete()

            messages.info(request, "Product is deleted")
            return redirect('main:index')
        return render(request, 'delete_product.html', {'product':product})
    else:
        messages.warning(request, "So'rov rad etildi!")
        return redirect('products:detail', product.id)
    
@login_required(login_url='login')
def newComment(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        Comment.objects.create(
            user=request.user,
            product=product,
            body=request.POST['body'],
        )

        return redirect('products:detail', product.id)
    return HttpResponse('Add comment')

@login_required(login_url='login')
def deleteComment(request, product_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.info(request, "Comment is deleted!")
        return redirect('products:detail', product_id)
    return redirect('products:detail', product_id)
    




