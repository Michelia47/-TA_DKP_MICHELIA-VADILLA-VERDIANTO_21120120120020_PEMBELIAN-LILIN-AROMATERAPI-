from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

def button1():
    pilihan=""

    while len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA")
        return    
    while (radio.get()== 0):
        messagebox.showerror("Error","BELUM MEMILIH VARIAN")
        return
    while len(stringjml.get())== 0:
        messagebox.showerror("Error","BELUM MENGISI JUMLAH")
        return
    
    if radio.get() == 1:
        jumlah=stringjml.get()
        harga=int(jumlah)*21000
        pilihan="\nLilin Aromaterapi Varian Lavender Rp 21.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 2:
        jumlah=stringjml.get()
        harga=int(jumlah)*21000
        pilihan="\nLilin Aromaterapi Varian Coconut Rp 21.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 3:
        jumlah=stringjml.get()
        harga=int(jumlah)*22000
        pilihan="\nLilin Aromaterapi Varian Vanila Rp 22.000,00\n "  + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"    
    elif radio.get() == 4:
        jumlah=stringjml.get()
        harga=int(jumlah)*22000
        pilihan="\nLilin Aromaterapi Varian Rose Rp 22.000,00\n "  + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 5:
        jumlah=stringjml.get()
        harga=int(jumlah)*22000
        pilihan="\nLilin Aromaterapi Varian Milk Rp 22.000,00\n "  + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"    
        
    elif radio.get() == 6:
        jumlah=stringjml.get()
        harga=int(jumlah)*23000
        pilihan="\nLilin Aromaterapi Varian Bubblegum Rp 23.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"    
    elif radio.get() == 7:
        jumlah=stringjml.get()
        harga=int(jumlah)*23000
        pilihan="\nLilin Aromaterapi Varian Green Tea Rp 23.000,00\n " +  "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 8:
        jumlah=stringjml.get()
        harga=int(jumlah)*24000
        pilihan="\nLilin Aromaterapi Varian Rice Milk Rp 24.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 9:
        jumlah=stringjml.get()
        harga=int(jumlah)*24000
        pilihan="\nLilin Aromaterapi Varian Aloevera Rp 24.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"    
    elif radio.get() == 10:
        jumlah=stringjml.get()
        harga=int(jumlah)*24000
        pilihan="\nLilin Aromaterapi Varian Melon Rp 24.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"    


    elif radio.get() == 11:
        jumlah=stringjml.get()
        harga=int(jumlah)*25000
        pilihan="\nLilin Aromaterapi Varian Honey and Mint Rp 25.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 12:
        jumlah=stringjml.get()
        harga=int(jumlah)*25000
        pilihan="\nLilin Aromaterapi Varian Chocoholic Rp 25.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 13:
        jumlah=stringjml.get()
        harga=int(jumlah)*26000
        pilihan="\nLilin Aromaterapi Varian Pepermint Rp 26.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 14:
        jumlah=stringjml.get()
        harga=int(jumlah)*26000
        pilihan="\nLilin Aromaterapi Varian Jasmine Rp 26.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"
    elif radio.get() == 15:
        jumlah=stringjml.get()
        harga=int(jumlah)*26000
        pilihan="\nLilin Aromaterapi Varian Apple Rp 26.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah            : " + stringjml.get() + " \nTotal                : Rp " + str(harga) +",00\n"

    if strmb.get() == 'Metode bayar ...':
        messagebox.showerror("Error","BELUM MEMILIH METODE BAYAR")
        return

    pesan = "== Selamat Datang di Rumah Lilin ==\n " + "\nBerikut Rincian Harga Satuan :" + pilihan + "Metode Bayar : " + strmb.get() + "\n" + "Atas Nama      : " + stringnama.get() + "\n" + "\nTerima Kasih dan Selamat Berbelanja !"
    messagebox.showinfo("Rincian", pesan)
  
top = Tk()
top.config(background = "light yellow")
top.geometry("600x600")
top.title("RUMAH LILIN")

#creating label
lbjudul = Label(top, text = "== RUMAH LILIN ==", font = "Times 14", background = "light blue")
lbjudul.pack()
lbjudul = Label(top, text = "== MENYEDIAKAN BERBAGAI VARIAN LILIN AROMATERAPI ==", font = "Times 14", background = "light blue")
lbjudul.pack()
lbjudul = Label(top, text = "Silahkan Isi Form Berikut Untuk Pembelian :", font = "Times 10", background = "pink").place(x = 20,y = 100)
lbjudul = Label(top, text = "Silahkan Masukkan Nama :", font = "Times 10", background = "pink").place(x = 20,y = 140)
lbjudul = Label(top, text = "Silahkan Pilih Varian :", font = "Times 10", background = "pink").place(x = 20,y = 220)
lbjudul = Label(top, text = "Silahkan Masukkan Jumlah dan Pilih Metode Pembayaran :", font = "Times 10", background = "pink").place(x = 20,y = 370)

lbnama = Label(top, text = "Nama Pembeli", font = "Times 10", background = "light blue").place(x = 20,y = 170)
lbc = Label(top, text = "Pilihan Varian",font = "Times 10", background = "light blue").place(x = 20, y=250)
lbjml = Label(top, text = "Jumlah", font = "Times 10", background = "light blue").place(x = 20, y=400)
lbbayar = Label(top, text = "Metode Bayar", font = "Times 10", background = "light blue").place(x = 20, y=440)

#create input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama, font = "Times 10", bd = 5).place(x = 120, y = 170)  

stringjml = StringVar()
ijml = Entry(top,width = 20, textvariable=stringjml, font = "Times 10", bd = 5).place(x = 120, y = 400)    
    
#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Lavender ( 21K )", font = "Times 10", background = "light blue" , variable=radio, value=1).place(x=120, y=250)  
R2 = Radiobutton(top, text="Coconut ( 21K )", font = "Times 10", background = "light blue" , variable=radio, value=2).place(x=120, y=270)  
R3 = Radiobutton(top, text="Vanila ( 22K )", font = "Times 10", background = "light blue" , variable=radio, value=3).place(x=120, y=290)
R4 = Radiobutton(top, text="Rose ( 22K )", font = "Times 10", background = "light blue" , variable=radio, value=4).place(x=120, y=310)
R5 = Radiobutton(top, text="Milk ( 22K )", font = "Times 10", background = "light blue" , variable=radio, value=5).place(x=120, y=330)

R6 = Radiobutton(top, text="Bubblegum ( 23K )", font = "Times 10", background = "light blue" , variable=radio, value=6).place(x=260, y=250)  
R7 = Radiobutton(top, text="Green Tea( 23K )", font = "Times 10", background = "light blue" , variable=radio, value=7).place(x=260, y=270)
R8 = Radiobutton(top, text="Rice Milk ( 24K )", font = "Times 10", background = "light blue" , variable=radio, value=8).place(x=260, y=290)  
R9 = Radiobutton(top, text="Aloevera ( 24K )", font = "Times 10", background = "light blue" , variable=radio, value=9).place(x=260, y=310)
R10 = Radiobutton(top, text="Melon ( 24K )", font = "Times 10", background = "light blue" , variable=radio, value=10).place(x=260, y=330)

R11 = Radiobutton(top, text="Honey and Mint ( 25K )", font = "Times 10", background = "light blue" , variable=radio, value=11).place(x=410, y=250)  
R12 = Radiobutton(top, text="Chocoholic ( 25K )", font = "Times 10", background = "light blue" , variable=radio, value=12).place(x=410, y=270)  
R13 = Radiobutton(top, text="Pepermint ( 26K )", font = "Times 10", background = "light blue" , variable=radio, value=13).place(x=410, y=290)  
R14 = Radiobutton(top, text="Jasmine ( 26K )", font = "Times 10", background = "light blue" , variable=radio, value=14).place(x=410, y=310)
R15 = Radiobutton(top, text="Apple ( 26K )", font = "Times 10", background = "light blue" , variable=radio, value=15).place(x=410, y=330)

#create combobox
strmb = StringVar(value='Metode bayar ...') 
Cb1 = ttk.Combobox(top, width = 18, textvariable = strmb, font = "Times 10", state="readonly")
Cb1.place(x=120, y=440)

# Adding combobox drop down list 
Cb1['values'] = ('Tunai',
                 'Kartu Kredit') 

#create button    
btn = Button(top, command = button1, text="LIHAT TOTAL", font = "Times 10", background = "light blue", activebackground="pink", bd = 5).place(x=120,y=500)
btn = Button(top, command = top.destroy, text="KELUAR", font = "Times 10", background = "light blue", activebackground="pink", bd = 5).place(x=230,y=500)

top.mainloop()
