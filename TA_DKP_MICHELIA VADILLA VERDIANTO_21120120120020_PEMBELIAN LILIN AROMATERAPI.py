from tkinter import * 
from tkinter import ttk
from tkinter import messagebox 

def button1():
    pilihan=""

    while len(stringnama.get()) == 0:
        messagebox.showerror("Error","BELUM MENGISI NAMA PEMBELI")
        return    
    while (radio.get()== 0):
        messagebox.showerror("Error","BELUM MEMILIH JENIS IKAN HIAS")
        return
    while len(stringjml.get())== 0:
        messagebox.showerror("Error","BELUM MENGISI JUMLAH")
        return
    
    if radio.get() == 1:
        jumlah=stringjml.get()
        harga=int(jumlah)*400000
        pilihan="\nIkan Cupang Avatar ( CA ) RP 400.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 2:
        jumlah=stringjml.get()
        harga=int(jumlah)*300000
        pilihan="\nIkan Cupang Black Samurai ( CBS ) Rp 300.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 3:
        jumlah=stringjml.get()
        harga=int(jumlah)*250000
        pilihan="\nIkan Cupang Hellboy ( CH ) Rp 250.000,00\n "  + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"    
    elif radio.get() == 4:
        jumlah=stringjml.get()
        harga=int(jumlah)*500000
        pilihan="\nIkan Cupang Blue Rim ( CBR ) Rp 500.000,00\n "  + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
        
    elif radio.get() == 5:
        jumlah=stringjml.get()
        harga=int(jumlah)*1000000
        pilihan="\nIkan Koi Tancho ( KT ) Rp 1.000.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"    
    elif radio.get() == 6:
        jumlah=stringjml.get()
        harga=int(jumlah)*800000
        pilihan="\nIkan Koi Shiro Utsuri ( KSU ) Rp 800.000,00\n " +  "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 7:
        jumlah=stringjml.get()
        harga=int(jumlah)*500000
        pilihan="\nIkan Koi Shusui ( KS ) Rp 500.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 8:
        jumlah=stringjml.get()
        harga=int(jumlah)*1500000
        pilihan="\nIkan Koi Ogon ( KO ) Rp 1.500.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"    


    elif radio.get() == 9:
        jumlah=stringjml.get()
        harga=int(jumlah)*200000
        pilihan="\nIkan Mas Koki Black Moor ( MKBM ) Rp 200.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 10:
        jumlah=stringjml.get()
        harga=int(jumlah)*135000
        pilihan="\nIkan Mas Koki Bubble Eye ( MKBE ) Rp 135.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 11:
        jumlah=stringjml.get()
        harga=int(jumlah)*250000
        pilihan="\nIkan Mas Koki Tosakin ( MKT ) Rp 250.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"
    elif radio.get() == 12:
        jumlah=stringjml.get()
        harga=int(jumlah)*200000
        pilihan="\nIkan Mas Koki Watonai ( MKW ) Rp 200.000,00\n " + "\nBerikut Rincian Pembelian : \n" + "Jumlah       : " + stringjml.get() + " \nTotal           : Rp " + str(harga) +",00\n"

    pesan = "Selamat Datang di Toko Ikan Hias Kami " + stringnama.get()+ "\n" + "\nBerikut Rincian Harga Satuan : " + pilihan + "Atas Nama : " + stringnama.get() + "\n" + "\nTerima Kasih dan Selamat Berbelanja !"
    messagebox.showinfo("Rincian", pesan)

  
top = Tk()
top.config(background = "light blue")
top.geometry("500x500")
top.title("TOKO IKAN HIAS KAMI")

#creating label
lbjudul = Label(top, text = "== TOKO IKAN HIAS KAMI ==", font = "Normal 15", background = "pink")
lbjudul.pack()
lbjudul = Label(top, text = "== MENYEDIAKAN IKAN CUPANG, KOI, DAN KOKI ==", font = "Normal 15", background = "pink")
lbjudul.pack()
lbjudul = Label(top, text = "Silahkan Isi Form Berikut Untuk Pembelian :", font = "Normal 12", background = "light blue").place(x = 20,y = 100)
lbjudul = Label(top, text = "Silahkan Masukkan Nama :", font = "Normal 12", background = "light blue").place(x = 20,y = 140)
lbjudul = Label(top, text = "Silahkan Pilih Jenis Ikan :", font = "Normal 12", background = "light blue").place(x = 20,y = 220)
lbjudul = Label(top, text = "Silahkan Masukkan Jumlah :", font = "Normal 12", background = "light blue").place(x = 20,y = 360)


lbnama = Label(top, text = "Nama Pembeli", font = "Normal 12", background = "pink").place(x = 20,y = 170)
lbc = Label(top, text = "Jenis Ikan Cupang",font = "Normal 12", background = "pink").place(x = 20, y=250)
lbk = Label(top, text = "Jenis Ikan Koi", font = "Normal 12", background = "pink").place(x = 420, y=250)
lbmk = Label(top, text = "Jenis Ikan Mas Koki", font = "Normal 12", background = "pink").place(x = 740, y=250)
lbjml = Label(top, text = "Jumlah", font = "Normal 12", background = "pink").place(x = 20, y=390)

#create input  
stringnama = StringVar()
inama = Entry(top,width = 20, textvariable=stringnama, bd = 5).place(x = 160, y = 170)  

stringjml = StringVar()
ijml = Entry(top,width = 20, textvariable=stringjml, bd = 5).place(x = 160, y = 390)    

#create radio
radio = IntVar()
R1 = Radiobutton(top, text="Ikan Cupang Avatar ( CA )", background = "light green" , variable=radio, value=1).place(x=160, y=250)  
R2 = Radiobutton(top, text="Ikan Cupang Black Samurai ( CBM )", background = "light green" , variable=radio, value=2).place(x=160, y=270)  
R3 = Radiobutton(top, text="Ikan Cupang Hellboy ( CH )", background = "light green" , variable=radio, value=3).place(x=160, y=290)
R4 = Radiobutton(top, text="Ikan Cupang Blue Rim ( CBR )", background = "light green" , variable=radio, value=4).place(x=160, y=310)

R5 = Radiobutton(top, text="Ikan Koi Tancho ( KT )", background = "yellow" , variable=radio, value=5).place(x=530, y=250)  
R6 = Radiobutton(top, text="Ikan Koi Shiro Utsuri ( KSU )", background = "yellow" , variable=radio, value=6).place(x=530, y=270)
R7 = Radiobutton(top, text="Ikan Koi Shusui ( KS )", background = "yellow" , variable=radio, value=7).place(x=530, y=290)  
R8 = Radiobutton(top, text="Ikan Koi Ogon ( KO )", background = "yellow" , variable=radio, value=8).place(x=530, y=310)


R9 = Radiobutton(top, text="Ikan Mas Koki Black Moor ( MKBM )", background = "orange" , variable=radio, value=9).place(x=890, y=250)  
R10 = Radiobutton(top, text="Ikan Mas Koki Bubble Eye ( MKBE )", background = "orange" , variable=radio, value=10).place(x=890, y=270)  
R11 = Radiobutton(top, text="Ikan Mas Koki Tosakin ( MKT )", background = "orange" , variable=radio, value=11).place(x=890, y=290)  
R12 = Radiobutton(top, text="Ikan Mas Koki Watonai ( MKW )", background = "orange" , variable=radio, value=12).place(x=890, y=310)  

#create button
btn = Button(top, command = button1, text="TOTAL", activebackground="pink", bd = 5).place(x=160,y=440)

top.mainloop()
