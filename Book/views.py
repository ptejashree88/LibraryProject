from django.shortcuts import render, redirect

from django.http import HttpResponse
from Book.models import Book
# Create your views here.

def homepage(request):
    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request, template_name = 'home.html', context = {"books" : all_books})

def save_book(request):
    print("In save book")
    print(request.POST)
    b_name = request.POST.get("name")
    b_auther = request.POST.get("auth")
    b_qty = request.POST.get("qty")
    b_price = request.POST.get("price")
    b_pub = request.POST.get("pub")
    # b_tr = request.POST.get("true")
    # b_fs = request.POST.get("false")
    # print(b_name, b_auther, b_qty, b_price, b_tr, b_fs)
    print(b_name, b_auther, b_qty, b_price, b_pub)


    
    if b_pub == "on":
        flag = True
    else:
        flag = False
    bk = Book(name = b_name, auther = b_auther, qty = b_qty, price = b_price, is_published = flag)             # to save book in database
    '''
    if b_tr =='on':
        flag = True
    elif b_fs == 'on':
        flag = False
    else:
        # raise Exception("Please select one option")
        return HttpResponse("Please select one option from True or False button")

    bk = Book(name = b_name, auther = b_auther, qty = b_qty, price = b_price, is_published = flag)             # to save book in database
    '''
    bk.save()
    return redirect("Welcome")

def edit_book(request, id):
    try:
        book_obj = Book.objects.get(id = id) 
    except Book.DoesNotExist:
        msg = f"No book found for id: {id}"
        return HttpResponse(msg)

    # all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.active_objects.all()
    return render(request, template_name = 'home.html', context = {"books" : all_books, "book" : book_obj})

def delete_book(request, pk):
    book_obj = Book.objects.get(id = pk)
    # book_obj.delete()
    book_obj.is_deleted = 'Y'
    book_obj.save()
    return redirect("Welcome")



def hard_delete_book(request, pk):
    book_obj = Book.objects.get(id=pk)
    book_obj.delete()
    return redirect('Welcome')


def restore_book(request, id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 'N'
    book_obj.save()
    return redirect('Welcome')


def show_deleted_data(request):
    all_deleted_books = Book.inactive_objects.all()  # thru custom manager
    return render(request, template_name='home.html', context={"books": all_deleted_books})

def delete_all_book(request):
    book = Book.active_objects.all()
    for bk in book:
        bk.is_deleted = 'Y'
        bk.save()
    return redirect('Welcome')

def restore_all_book(request):
    book = Book.inactive_objects.all()
    for bk in book:
        bk.is_deleted = 'N'
        bk.save()
    return redirect('Welcome')

