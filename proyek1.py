
def coulomb2(f,q2,r):
    k=9*10**9
    q1=f*r**2/q2*k
    print(q1)
#resistor tanpa sum
def resistor(a,b,c,d):
    seri=a+b+c+d
    pararel=1/a+1/b+1/c+1/d
    print("seri=",seri)
    print("pararel",pararel)
#soal 4 gaya coulomb
def coulomb(q1,q2,r):
    f=(9*10**9*(q1*10**(-6)*(q2*10**-6))/(r/100)**2)
    print("gaya adalah:" ,f)
#soal 7  kalor perubahan energi panas
def kalor(m,c,t):
    w=m*c*t
    print(w)
#soal 2 persamaan 1 linear
def linear1(x,a,b):
    y = a * x + b
    print(f"Hasil dari persamaan {a}x + {b} adalah {y}")
#soal 5 gempa
def gempa(magnitude):
    if (magnitude > 8):
        print("gempa sangat besar")
    elif(magnitude >= 7 and magnitude <=8):
        print("gempa besar")
    elif(magnitude >=5 and magnitude <=6):
        print("gempa merusak")
    elif(magnitude >=4 and magnitude <5):
        print("gempa sedang")
    elif(magnitude >=3 and magnitude <4):
        print("gema bumi kecil")
    elif(magnitude >=1 and magnitude <3):
        print("gempa bumi mikro")
    elif(magnitude <1):
        print("gempa bumi ultra mikro")
#soal 20 persamaan 2 linear
def linear2(a1, x, a2, y, operator):
    if operator == '*':
        if (a1 * x == a2 * y):
            print("Jawaban benar")
        else:
            print("Jawaban salah")
    elif operator == '+':
        if (a1 + x == a2 + y):
            print("Jawaban benar")
        else:
            print("Jawaban salah")
    elif operator == '-':
        if (a1 - x == a2 - y):
            print("Jawaban benar")
        else:
            print("Jawaban salah")
    else:
        print("Operator matematika tidak valid")
#soal 18 mengkategorikan sudut segitiga
def jenis_sudut(c):
    if (c < 90):
        print ("sudut lancip")
    elif (c == 90):
        print("sudut siku-siku")
    elif(c > 180 or c < 0):
        print("bukan segitiga")
#soal 17 pythagoras segitiga
def pythagoras(a,b):
    c=(a**2+b**2)**0.5
    print("nilai c:",c)
#soal 8 tekanan
def tekanan(p,q,h):
    tekana=p*q*h
    print('tekanan=',tekana)
def gaya_apung(p,v,q):
    apung=p*q*v
    print("gaya apung=",apung)
#soal 16 kalor
def kalor(m,g,h):
    kalor=m*g*h
    print("kalor=",kalor)
#soal 6  energi kinetik
def kal(m,v):
    m=0.5*m*v**2
    print(m)
    
#s0al 8 energi potensial, mekanik
def energi_potensial(m,g,h):
    ep=m*g*h
    print("energi potensial=",ep)

def energi_mekanik(ek,ep):
    em=ek+ep
    print("energi mekanik=",em)
    
#soal 14 celcius ke suhu lain
def celcius(c):
    k=c+273
    r=(4/5)*c
    f=(c*9/5)+32
    print(f,"farenheit,",r,"reamur,",k,"kelvin.")

def farenheit(f):
    c=(f-32)*5/9
    k=(f+459.67)*5/9
    r=4/9*(f-32)
    print(c,"celcius,",k,"kelvin,",r,"reamur")

def kelvin(k):
    c=k-273
    f=(k*9/5)-459.67
    r=4/5*(k-271)
    print(c,"celcius,",f,'farenheit,',r,"reamur")

def reamur(r):
    c=r/0.8
    f=(r*2.25)+32
    k=(r/0.8)+273.15
    print(c,"celcius,",f,'far2enheit,',k,"kelvin")
#soal 10

    
    
ulang = 'ya'
while (ulang =='ya'):
    print("pilih")
    print("soal wajib")
    print("1.persamaan linear 1 variabel(ax+b)")
    print("2.gaya coulomb")
    print("3.kalor (perubahan energi panas)")
    print("4.gempa")
    print("5.mencari sudut segitiga")
    print("6.persamaan 2 linear(membuktikan kebenaran)")
    print("7.resistor")
    print("soal tambahan")
    print("9.pythagoras mencari nilai c")
    print("10.tekanan")
    print("11.kalor(perubahan energi panas)")
    print("12.kalor")
    print("13.energi potensial dan mekanik")
    print("14.suhu")
    pilih =float(input("masukan angka pilihan anda="))
    if(pilih == 2):
        f=int(input("masukan gaya coulomb="))
        q2=int(input("masukan q2 (besar muatan 2) dalam mikro="))
        r=int(input("masukan r (jarak) dalam m="))
        coulomb2(f,q2,r)
    elif(pilih == 3):
        m=int(input("masukan massa benda="))
        c=int(input("masukan kalor jenis"))
        t=int(input("masukan perubahan suhu="))
        kalor(m,c,t)
    elif(pilih == 1):
        a = int(input("Masukkan nilai koefisien a: "))
        b = int(input("Masukkan nilai koefisien b: "))
        x = int(input("Masukkan nilai x: "))
        linear1(x,a,b)
    elif(pilih == 4):
        magnitude=float(input("masukan magnitudo="))
        gempa(magnitude)
    elif(pilih == 5):
        c = int(input("Masukkan panjang sisi c (sisi miring): "))
        jenis_sudut(c)
    elif(pilih == 6):
        a1 = int(input("Masukkan nilai a1: "))
        x = int(input("Masukkan nilai x: "))
        a2 = int(input("Masukkan nilai a2: "))
        y = int(input("Masukkan nilai y: "))
        operator = input("Masukkan operator matematika (+ , - , *: ")
        linear2(a1, x, a2, y, operator)
    elif(pilih == 7):
        a=int(input("Masukkan nilai resistor ke 1 (ohm): "))
        b=int(input("Masukkan nilai resistor ke 2 (ohm): "))
        c=int(input("Masukkan nilai resistor ke 3 (ohm): "))
        d=int(input("Masukkan nilai resistor ke 4 (ohm): "))
        resistor(a,b,c,d)
    elif(pilih == 9):
        a=int(input("masukan nilai a="))
        b=int(input("masukan nilai b="))
        pythagoras(a,b)
    elif(pilih == 10):
        print("1.tekanan")
        print("2.gaya apung")
        print("pilih 1/2")
        pilihan=int(input("masukan pilihan="))
        if (pilihan == 1):
            p=int(input("masukan massa jenis="))
            q=int(input("masukan gravitasi="))
            h=int(input("masukan kedalaman="))
            tekanan(p,q,h)

        elif (pilihan == 2):
            p=int(input("masukan massa jenis="))
            v=int(input("masukan volume="))
            q=int(input("masukan percepatan gravitasi="))
            gaya_apung(p,v,q)
    elif(pilih == 11):
        m=int(input("masukan massa benda="))
        g=int(input("masukan kalor jenis="))
        h=int(input("masukan perubahan suhu="))
        kalor(m,g,h)
    elif(pilih == 12):
        m=int(input("masukan"))
        v=int(input("masukan"))
        kal(m,v)
    elif(pilih== 13):
        m=int(input("masukan massa benda="))
        g=int(input("masukan percepatan gravitasi="))
        h=int(input("masukan ketinggian benda="))
        energi_potensial(m,g,h)
        ek=int(input("masukan energi kinetik="))
        ep=int(input("masukan energi potensial= "))
        energi_mekanik(ek,ep)
    elif(pilih==14):
        print("pilih suhu yang ingin di konversi")
        print("1.celcius")
        print("2.farenheit")
        print("3.kelvin")
        print("4.reamur")
        pilihan=int(input("masukan pilihan="))
        if(pilihan == 1):
            c=int(input("masukan suhu="))
            celcius(c)
        elif(pilihan == 2):
            f=int(input("masukan suhu="))
            farenheit(f)
        elif(pilihan == 3):
            k=int(input("masukan suhu="))
            kelvin(k)
        elif(pilihan == 4):
            r=int(input("masukan suhu="))
            reamur(r)

    else:   
        print("pilihan anda tidak ada")
    ulang = str(input("ulang? (ya/tidak)"))
