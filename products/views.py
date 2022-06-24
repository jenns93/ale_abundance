from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from .models import Product, Category, Review_Product
from .forms import ProductForm

from django.db.models.functions import Lower
import random
# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()
    product_reviews = Review_Product.objects.filter(product=product_id)
    sort = None
    categories = None
    direction = None

    items = list(Product.objects.all())

    random_items = random.sample(items, 4)
    is_favourite = False

    if product.favourites.filter(pk=request.user.id).exists():
        is_favourite = True

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
  
    context = {
        'product': product,
        'products': products,
        'product_reviews': product_reviews,
        'current_categories': categories,
        'random_items': random_items,
        'is_favourite': is_favourite,
        
    }
    
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Product editing: {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))
    else:
        messages.warning(request, f'Confirm deletion: {product.name}')

    template = 'products/delete_product.html'
    context = {
        'product': product,
    }

    return render(request, template, context)
    

@login_required
def favourite_add(request, product_id):
    """ Add to favourites """
    product = get_object_or_404(Product, pk=product_id)
    products = Product.objects.all()

    if product.favourites.filter(pk=request.user.id).exists():
        product.favourites.remove(request.user)
        messages.info(request, f'{product.name} removed from favourites!')
    else:
        product.favourites.add(request.user)
        messages.info(request, f'{product.name} added to favourites!')

    context = {
        'products': products,
        }

    return render(request, 'products/products.html', context)


@login_required
def fav_list(request):
    """ favourite list view """
    user = request.user
    allfav = user.favourite.all()

    context = {
        'allfav': allfav, } 
    return render(request, 'products/favourites_list.html', context)

    
def product_review(request, product_id):
    """ post product review """
    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review_Product.objects.all()
    products = Product.objects.all()
    
    if request.method == 'POST':
        stars = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        prodreview = Review_Product.objects.create(product=product, user=request.user, stars=stars, content=content)

        context = {'products': products, 'prodreview': prodreview, 'product': product }
        messages.info(request, f'Rewview for: {product.name} successfully posted!')
        return render(request, 'products/products.html', context)
        
    else:
        context = {'products': products,  'product': product }
        return render(request, 'products/review_product.html', context)

def page_not_found_view(request, exception):
    """ 404 view """
    return render(request, '404.html', status=404)