import threading
import datetime
import queue
import urllib.request
import xlsxwriter
import sys
import os

def ex(nameoffile,listof):
    listofj=listof

    workbooke = xlsxwriter.Workbook(nameoffile+".xlsx", {'constant_memory': True})
    worksheete = workbooke.add_worksheet()
    worksheete.set_column('A:A', 10)#뉴스사0
    worksheete.set_column('B:B', 100)#제목1
    worksheete.set_column('C:C', 10)#url2

    #맨위 설정
    worksheete.write("A1","날짜")
    worksheete.write("B1","텍스트")
    worksheete.write("C1","ID")

    yu=1
    for x in listofj:
        yu+=1
        celc="C"+str(yu)
        cela="A"+str(yu)
        celb="B"+str(yu)


        worksheete.write(cela,x[0])
        worksheete.write(celb,x[1])
        worksheete.write(celc,x[2])


    workbooke.close()
    print("완료")
