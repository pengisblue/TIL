from django.shortcuts import render

# Create your views here.
book_list = [
        {'author': '김시습', 'book_list': ['금오신화', '이생규장전', '만복자서포기']}, 
        {'author': '허균', 'book_list': ['홍길동전', '장생전', '도문대작']},  
        {'author': '남영로', 'book_list': ['옥루몽', '옥련몽']}, 
        {'author': '작자 미상', 'book_list': ['장화홍련전', '가락국 신화', '온달 설화']}, 
        {'author': '임제', 'book_list': ['수성지', '백호집', '원생몽유록']}
    ]

def index(request):
    context = {
        'book_list': book_list,
    }
    return render(request, 'books/index.html', context)

def author_info(request, author):
    for i in range(len(book_list)):
        if author == book_list[i]['author']:
            write_books = book_list[i]['book_list']
            break

    context = {
        'author': author,
        'write_books': write_books
    }
    return render(request, 'books/author.html', context)