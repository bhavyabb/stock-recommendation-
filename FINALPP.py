from tkinter import *
import yfinance as yf 
import matplotlib.pyplot as plt 
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
root = Tk()
root.geometry("600x400")
def stockgraph():
    start_date = '1990-01-01'
    end_date = '2021-07-12'
    # Ticker Name (Stock name )
    ticker = stockn.get()
    data = yf.download(ticker, start_date, end_date)
    data['Adj Close'].plot()

    # label
    plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)

    # labels for  x-axis and y-axis
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)

    # Grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

    plt.show()
def compgraph():
    start_date = '1990-01-01'
    end_date = '2021-07-12'

    tickers_list = stockn.get().split(",")
    data = pd.DataFrame(columns=tickers_list)
    a = 0
    for ticker in tickers_list:
        data[ticker] = yf.download(ticker, start_date,end_date)['Adj Close']
    data.plot()
     # label
    plt.title("Comparing performance of stocks")

    # labels for  x-axis and y-axis
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)

    # Grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.show()
#Driver Code
def rec():
    start_date = '1990-01-01'
    end_date = '2021-07-12'
    tickers_list = stockn.get().split(",")
    data = pd.DataFrame(columns=tickers_list)
    a = 0
    for ticker in tickers_list:
       data[ticker] = yf.download(ticker, start_date,end_date)['Adj Close']
    fin = data.max().sort_values(ascending=FALSE)
    #fin = recom.max()
    recLabel = Label(root,text=f"Based on the annulised returns we recommend the stock {fin[:2]}")
    recLabel.grid(row=4,column=2)
   
    

title = Label(root,text="Welcome to Kenobi's Analytics",font="1")
title.grid(row=0,column=2)
stockn = Entry(root)
stockn.insert(0,"Enter Stock code")
stockn.grid(row=1,column=2)
empty = Label(root,text="")
empty.grid(row=2,column=0)
sLabel1=Label(root,text="Analyse a single stock",font="20")
sLabel1.grid(row=2,column=1)
sButton1=Button(master=root,text="Analyse",command = stockgraph,font="20")
sButton1.grid(row=2,column=2)
sLabel2=Label(root,text="Compare multiple stocks")
sLabel2.grid(row=2,column=3)
sButton2=Button(master=root,text="Analyse",command = compgraph,font="20")
sButton2.grid(row=2,column=4)
recbutton = Button(master=root,text="Our experct recommendations",command=rec)
recbutton.grid(row=3,column=2)
#Crewating an infinite loop which runs till we hit the 'X' button 
root.mainloop()