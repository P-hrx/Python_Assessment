from django.http import response,JsonResponse
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404



import time

from .models import Product
from .models import Contact
from .models import Orders
from .models import OrderUpdate
from math import ceil
import json

 # Create your views here.
def index(request):

    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat).order_by('-pub_date')[1:]

        n = len(prod)

        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1,nSlides),nSlides])

    
    params = {'allProds':allProds}
    #print(prod)

    return render(request, 'shop/index.html',params)
def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contacts = Contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
    return render(request, 'shop/contact.html')

def searchmatch(query,item):
        if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
            return True
        else:
            False


def search(request):
    query = request.GET.get('search')
    allProds = []
    prod=[]
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        for item in prodtemp:
            if searchmatch(query,item) == True:
                prod.append(item)

        n = len(prod)

        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
    allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def productView(request, myid):
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodview.html', {'product':product[0]})




def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state,
                       zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')


def add_contacts(request):
    begin = time.time()
    #contact_list=[['name':'A','email':'sde','mobile':5432,'desc':'fcvdssf'],['B','sde',94132,'xxvxcsf'],['C','sde',9232,'fhjjhsf'],['D','sde',9032,'dfgddrejsf']]
    contact_list = [{'name': '1', 'email': 'email1', 'phone': 331, 'desc':'testing1'},
                        {'name': '2', 'email': 'email2', 'phone': 332, 'desc':'testing2'},
                        {'name': '3', 'email': 'email3', 'phone': 333, 'desc':'testing3'},
                        {'name': '4', 'email': 'email4', 'phone': 334, 'desc':'testing4'},
                        {'name': '5', 'email': 'email5', 'phone': 335, 'desc':'testing5'},
                        {'name': '6', 'email': 'email6', 'phone': 336, 'desc':'testing6'},
                        {'name': '7', 'email': 'email7', 'phone': 337, 'desc':'testing7'},
                        {'name': '8', 'email': 'email8', 'phone': 338, 'desc':'testing8'},
                        {'name': '9', 'email': 'email9', 'phone': 339, 'desc':'testing9'},
                        {'name': '10', 'email': 'email10', 'phone': 340, 'desc':'testing10'},
                        {'name': '11', 'email': 'email11', 'phone': 341, 'desc':'testing11'},
                        {'name': '12', 'email': 'email12', 'phone': 342, 'desc':'testing12'},
                        {'name': '13', 'email': 'email13', 'phone': 343, 'desc':'testing13'},
                        {'name': '14', 'email': 'email14', 'phone': 344, 'desc':'testing14'}]
    #ratings_dictionary = {'book_one': 10, 'book_two': 20, 'book_three': 30}
    objct_list=[Contact(**contact_dict) for contact_dict in contact_list]
    #data_list = [{name: 'abc'}, {name: 'xyz'}]
    #obj_list = [MyModal(**data_dict) for data_dict in data_list]
    objs = Contact.objects.bulk_create(objct_list)
    # for contacts in contact_list:

    #     contact_object = Contact()
    #     contact_object.name = contacts['name']
    #     contact_object.email = contacts['email']
    #     contact_object.phone = contacts['phone']
    #     contact_object.desc = contacts['desc']
    #     contact_object.save()


    # print(contacts[0])
    # print(contacts[1])
    # print(contacts[2])
    # print(contacts[3])
    # contact.name=contacts[0]
    # contact.email=contacts[1]
    # contact.phone=contacts[2]
    # contact.desc=contacts[3]
    # contact.save()
    end = time.time()
    time_taken = end - begin
    return HttpResponse(time_taken)


def show_contacts(request):
    list = []
    contacts=Contact.objects.values('msg_id','name','email','phone','desc')
    #print(contacts)
    # context={ 
    #     'object_list':contacts
    #      }
    
    return HttpResponse(contacts) 