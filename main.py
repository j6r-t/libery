from PyQt5.QtWidgets import QMainWindow, QApplication, QDateEdit,QMessageBox
from PyQt5.uic import loadUi 
import csv 
from book_class import book
def alert(msg):
    m=QMessageBox()
    m.setText(msg)
    m.exec()
    
    
def add_book():
    #id_b=w.name_book.text()
   
    name_book=w.name_book.text()
    auther_book=w.auther_book.text()
    price=w.price.text()
    number_page=w.number_page.text()
    rel_date=w.rel_date.date().toPyDate()
    cat=w.cat.currentText()
    quant=w.quant.value()
    #index=w.cat.currentIndex()
    book1 = book(name_book=name_book,
             auther_book=auther_book,
             number_page=number_page,
             cat=cat,
             price=price,
            quant=quant,
            rel_date=rel_date)
    #print(book.__repr__(book1))
    print(book.id_maker(book1))





app=QApplication([])
w=loadUi("mainui.ui")
w.show()
w.eng.clicked.connect(add_book)
app.exec_()
