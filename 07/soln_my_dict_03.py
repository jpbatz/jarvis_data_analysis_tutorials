book = {}
for item in ['title', 'author', 'subject', 'num_pages']:
    book[item] = input('Please provide the ' + item + ': ')

print(book)


book = {}
for item in ['title', 'author', 'subject', 'num_pages']:
    if item == 'num_pages':
        book[item] = int(input('Please provide the ' + item + ': '))    
    else: 
        book[item] = input('Please provide the ' + item + ': ')
        
print(book) 

print(book.get('format', 'hardback'))

book.setdefault('publisher', "O'Reilly")

print(book)
