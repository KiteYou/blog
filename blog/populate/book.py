from populate import base
from article.models import Book
import random
import datetime

def populate():
    print('Populating Book', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django',
              '如何像電腦科學家一樣思考2', '10 分鐘內學好 Python3', '簡單學習 Django4',
              '如何像電腦科學家一樣思考2', '10 分鐘內學好 Python3', '簡單學習 Django4',
              '如何像電腦科學家一樣思考2', '10 分鐘內學好 Python3', '簡單學習 Django4',]
    author = ['作者1' '作者2' '作者3']
    Book.objects.all().delete()
    for title in titles:
        book = Book()
        book.title = title
        book.author = author [random.randint(0, len(author)-1)]
        book.publisher = author [random.randint(0, len(author)-1)]
        book.publishdate = datetime.datetime.today()
        book.printing = '1'
        book.price = '1000'
        book.save()
    
    print('done')
    
if __name__ == '__main__':
    populate()