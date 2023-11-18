import csv 

class book:
    all=[] 
    def __init__(self,name_book,auther_book,number_page,cat,price,quant,rel_date):
            self.name_book=name_book
            self.auther_book=auther_book
            self.number_page=number_page
            self.cat=cat
            self.price=price
            self.quant=quant
            self.rel_date=rel_date
            #self.id_book=self.id_maker(name_book,auther_book,number_page,rel_date)
    def __repr__ (self):
        return f"{self.__class__.__name__} ({self.name_book},{self.auther_book},{self.number_page},{self.cat},{self.price},{self.quant},{self.rel_date})"
       #     return f"{self.__class__.__name__} ({self.name_book},{self.auther_book},{self.number_page},{self.cat},{self.price},{self.quant},{self.rel_date},{self.id_book})"

    
    
    def id_maker(self):
        #craete id book
        #the first letter of the (book,auther,np)+nbline(two numbers)
        name= self.name_book[:2]
        auth=self.auther_book[:2]
        nb=str(self.number_page)
        nb=nb[:2]
        date=self.rel_date
        dat=date[:2]+date[7:]
        return f"{name}{auth}{nb}{dat}"
    
    def ist_repeated(self):
        #search if the book is repeated in the data 
        pass
    
    
# book1 = book(name_book="janjon",
#              auther_book="jesser",
#              number_page=210,
#              cat="12-01-2004",
#              price=100, quant=5,
#              rel_date="2023-11-16")
# 
# print(book.id_maker(book1))
