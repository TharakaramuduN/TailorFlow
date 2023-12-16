from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse, JsonResponse
from .models import *
from django.db.models import Count, Q, F
from itertools import groupby
import json
from django.core.paginator import Paginator


def home_view(request):
    return render(request, "pages/home.html", context={'title': "Home"})


def base_view(request):
    return render(request, "base.html", context={'title': 'Base View'})


def new_customer1(request):
    if request.method == 'POST':
        try:
            # Get form data from request.POST dictionary
            name = request.POST.get('Name')
            village = request.POST.get('Village')
            phone = request.POST.get('Phone')
            gmail = request.POST.get('Gmail')
            print(gmail)
            profilephoto = request.FILES.get('profilephoto')

            # Create Customers instance
            customer = Customers.objects.create(
                Name=name, Village=village, Phone=phone, Gmail=gmail, profilephoto=profilephoto)

            # Get measurement data
            neck = request.POST.get('Neck')
            chest = request.POST.get('Chest')
            waist = request.POST.get('Waist')
            hips = request.POST.get('Hips')
            thigh = request.POST.get('Thigh')
            knee = request.POST.get('Knee')
            calf = request.POST.get('Calf')
            sleeve = request.POST.get('Sleeve')
            back = request.POST.get('Back')
            waistband = request.POST.get('WaistBand')
            outseam = request.POST.get('Outseam')
            inseam = request.POST.get('Inseam')
            ankle = request.POST.get('Ankle')

            # Create Measurements instance
            measurement = Measurements.objects.create(customer=customer, Neck=neck, Chest=chest, Waist=waist,
                                                      Hips=hips, Thigh=thigh, Knee=knee, Calf=calf, Sleeve=sleeve,
                                                      Back=back, Waistband=waistband, Outseam=outseam, Inseam=inseam,
                                                      Ankle=ankle)

            # # Get product data
            # products_data = request.POST.get('products_data')
            # products_data_json = json.loads(products_data)
            # for product in products_data_json:
            #     print(product[])
            #     x = Products.objects.create(customer=customer, product_name=product['product_name'],
            #                                 garment_drop_off=product['garment_drop_off'], requested_pick_up_date=product['requested_pick_up_date'], price=product['price'], clothimage=product['clothimage'], design=product['design'])

            # Retrieve and handle each product data
            product_index = 0
            while f'product_name_{product_index}' in request.POST:
                product_name = request.POST.get(
                    f'product_name_{product_index}')
                garment_drop_off = request.POST.get(
                    f'garment_drop_off_{product_index}')
                requested_pick_up_date = request.POST.get(
                    f'requested_pick_up_date_{product_index}')
                price = request.POST.get(f'price_{product_index}')
                clothimage = request.FILES.get(f'cloth_image_{product_index}')
                design = request.FILES.get(f'design_{product_index}')
                print(product_name, garment_drop_off,
                      requested_pick_up_date, price, clothimage, design)

                # Save product instance
                Products.objects.create(
                    customer=customer,
                    product_name=product_name,
                    garment_drop_off=garment_drop_off,
                    requested_pick_up_date=requested_pick_up_date,
                    price=price,
                    clothimage=clothimage,
                    design=design
                )

                product_index += 1

            # Get transaction data
            amount = request.POST.get('amount')
            payment_date = request.POST.get('paymentdate')
            total_amount = request.POST.get('total')
            advance_amount = request.POST.get('advance')

            # Create Transactions instance
            transaction = Transactions.objects.create(customer=customer, amount=amount, payment_date=payment_date,
                                                      total_amount=total_amount, advance_amount=advance_amount)

            # Redirect to a success page or do something else
            return redirect('/')
        except Exception as e:
            # Handle any exceptions or errors here
            print(e)  # Log the error for debugging purposes
            print(request.POST.get('Gmail'))
            return HttpResponse("An error occurred while processing your request. Please try again later.")

    return render(request, "pages/newcustomer1.html", context={'title': 'Add Customer'})


def check_email_exists(request, customer_id=None):
    if request.method == 'GET':
        gmail = request.GET.get('gmail', None)
        if customer_id:
            user_exists = Customers.objects.exclude(
                customer_id=customer_id).filter(Gmail=gmail).exists()
        else:
            user_exists = Customers.objects.filter(Gmail=gmail).exists()
        return JsonResponse({'exists': user_exists})
    return JsonResponse({'error': 'Invalid request method.'})


def check_phone_exists(request, customer_id=None):
    if request.method == 'GET':
        phone = request.GET.get('phone', None)
        if customer_id:
            user_exists = Customers.objects.exclude(
                customer_id=customer_id).filter(Phone=phone).exists()
        else:
            user_exists = Customers.objects.filter(Phone=phone).exists()
        return JsonResponse({'exists': user_exists})
    return JsonResponse({'error': 'Invalid request method.'})


def customers(request):
    page = request.GET.get('page', 1)
    sort_param = request.GET.get('sort', 'created_at')
    customers = Customers.objects.all().order_by(sort_param)

    search_query = request.GET.get('search', '')
    if search_query:
        customers = customers.filter(
            Q(Name__icontains=search_query) |
            Q(Gmail__icontains=search_query) |
            Q(Phone__icontains=search_query) |
            Q(Village__icontains=search_query)
        )
    items_per_page = 7
    paginatitor = Paginator(customers, items_per_page)
    customers = paginatitor.page(page)
    return render(request, 'pages/customers.html', context={'title': 'Customers', 'customers': customers, 'search_query': search_query, 'sort_param': sort_param})


def customer_measurements(request, customer_id):
    name = Customers.objects.get(customer_id=customer_id)
    customer = Measurements.objects.get(customer_id=customer_id)
    return render(request, 'pages/customermeasurements.html', context={'title': 'Measurements', 'customer': customer, 'name': name.Name})


def edit_customers(request, customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    measurements = Measurements.objects.get(customer=customer)
    # products = Products.objects.get(customer=customer)
    # transactions = Transactions.objects.get(customer=customer)
    if request.method == 'POST':
        try:
            # Update customer data
            customer.Name = request.POST.get('Name')
            customer.Village = request.POST.get('Village')
            customer.Phone = request.POST.get('Phone')
            customer.Gmail = request.POST.get('Gmail')
            customer.save()

            # Update measurement data
            measurements.Neck = request.POST.get('Neck')
            measurements.Chest = request.POST.get('Chest')
            measurements.Waist = request.POST.get('Waist')
            measurements.Hips = request.POST.get('Hips')
            measurements.Thigh = request.POST.get('Thigh')
            measurements.Knee = request.POST.get('Knee')
            measurements.Calf = request.POST.get('Calf')
            measurements.Sleeve = request.POST.get('Sleeve')
            measurements.Back = request.POST.get('Back')
            measurements.Waistband = request.POST.get('WaistBand')
            measurements.Outseam = request.POST.get('Outseam')
            measurements.Inseam = request.POST.get('Inseam')
            measurements.Ankle = request.POST.get('Ankle')
            measurements.save()

            # Update product data
            # products.product_name = request.POST.get('productname')
            # products.garment_drop_off = request.POST.get('garmentdropoff')
            # products.requested_pick_up_date = request.POST.get(
            #     'requestedpickup')
            # products.garment_pick_up = request.POST.get('garmentpickup')
            # products.save()

            # # Update transaction data
            # transactions.amount = request.POST.get('amount')
            # transactions.payment_date = request.POST.get('paymentdate')
            # transactions.total_amount = request.POST.get('total')
            # transactions.advance_amount = request.POST.get('advance')
            # transactions.save()
            # # Redirect to a success page or do something else
            return HttpResponse("Updated Successfully")
        except Exception as e:
            # Handle any exceptions or errors here
            print(e)  # Log the error for debugging purposes
            return HttpResponse("An error occurred while processing your request. Please try again later.")
    return render(request, 'pages/editcustomers.html', context={
        'title': 'Edit Customer',
        "id": customer_id,
        "customer": customer,
        "measurements": measurements,
        # "products": products,
        # "transactions": transactions,
    })


def orders(request):
    page = request.GET.get('page', 1)
    filter_by = request.GET.get('filter', '')
    sort_param = request.GET.get('sort', 'requested_pick_up_date')
    search_query = request.GET.get('search', '')
    products = Products.objects.all()
    if filter_by and filter_by == 'groupby_customer':
        products = products.values('customer').annotate(
            num_products=Count('product_id'),
            customer_name=F('customer__Name'),
            customer_id=F('customer__customer_id')
        )
    print(products)
    products = products.order_by(
        sort_param, 'requested_pick_up_date')
    if search_query:
        products = products.filter(
            Q(product_name__icontains=search_query) |
            Q(price__icontains=search_query) |
            Q(customer__Name__icontains=search_query)
        )
    items_per_page = 7
    paginator = Paginator(products, items_per_page)
    products = paginator.page(page)

    return render(request, 'pages/orders.html', context={
        'title': 'Orders',
        'products': products,
        'sort_param': sort_param,
        'search_query': search_query,
        'filter_param': filter_by,
    })


def add_products(request, customer_id):
    customer = Customers.objects.get(customer_id=customer_id)
    if request.method == 'POST':
        # Get product data
        product_index = 0
        while f'product_name_{product_index}' in request.POST:
            product_name = request.POST.get(
                f'product_name_{product_index}')
            garment_drop_off = request.POST.get(
                f'garment_drop_off_{product_index}')
            requested_pick_up_date = request.POST.get(
                f'requested_pick_up_date_{product_index}')
            price = request.POST.get(f'price_{product_index}')
            clothimage = request.FILES.get(f'cloth_image_{product_index}')
            design = request.FILES.get(f'design_{product_index}')
            print(product_name, garment_drop_off,
                  requested_pick_up_date, price, clothimage, design)

            # Save product instance
            Products.objects.create(
                customer=customer,
                product_name=product_name,
                garment_drop_off=garment_drop_off,
                requested_pick_up_date=requested_pick_up_date,
                price=price,
                clothimage=clothimage,
                design=design
            )
            product_index += 1
        return HttpResponse('Products added successfully.')
    return render(request, 'pages/addproducts.html', context={'title': 'Add Product', 'id': customer_id})


def delete_customer(request, customer_id):
    customer = Customers.objects.filter(customer_id=customer_id)
    if customer:
        customer.delete()
        return JsonResponse({'message': 'Customer deleted successfully'})
