import sys

import pyDes as pyDes
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import random
import rsa

class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("menu.ui",self)
        self.mono.clicked.connect(self.monofunction)
        self.macierz.clicked.connect(self.macierzfunction)
        self.poli.clicked.connect(self.polifunction)
        self.base64.clicked.connect(self.base64function)
        self.hamming.clicked.connect(self.hammingfunction)
        self.rsa.clicked.connect(self.rsafunction)
        self.rsa_plik.clicked.connect(self.rsa_plikfunction)
        self.des.clicked.connect(self.desfunction)
        self.rc4.clicked.connect(self.rc4function)

    def monofunction(self):
        mono=Mono()
        widget.addWidget(mono)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def macierzfunction(self):
        macierz=Macierz()
        widget.addWidget(macierz)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def polifunction(self):
        poli=Poli()
        widget.addWidget(poli)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def base64function(self):
        base64=Base64()
        widget.addWidget(base64)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def hammingfunction(self):
        hamming=Hamming()
        widget.addWidget(hamming)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def rsafunction(self):
        rsa=RSA()
        widget.addWidget(rsa)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def rsa_plikfunction(self):
        rsa_plik=RSA_plik()
        widget.addWidget(rsa_plik)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def desfunction(self):
        des=DES()
        widget.addWidget(des)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def rc4function(self):
        rc4=RC4()
        widget.addWidget(rc4)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Mono(QDialog):
    def __init__(self):
        super(Mono,self).__init__()
        loadUi("mono.ui",self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text().lower()
        wiadomość_zaszyfrowana = self.lineEdit_2.text()

        alfabet = 'abcdefghijklmnopqrstuvwxyz '
        przesuniecie = 3

        lista = []

        for znak in wiadomość:
            if znak in alfabet:
                if znak == " ":
                    zmieniony_znak = " "
                else:
                    przesunięcie_index = (alfabet.index(znak) + przesuniecie) % len(alfabet)
                    zmieniony_znak = alfabet[przesunięcie_index]
                lista.append(zmieniony_znak)
            else:
                print("Nieprawidłowy znak:", znak)

        wynik = "".join(lista)
        self.lineEdit_2.setText(wynik)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Macierz(QDialog):
    def __init__(self):
        super(Macierz,self).__init__()
        loadUi("macierz.ui",self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text().lower()
        wiadomość_zaszyfrowana = self.lineEdit_2.text()

        wiadomość = wiadomość.replace(' ', '_')
        rozmiar_macierzy = int(len(wiadomość) ** 0.5) + 1
        macierz = [['!' for j in range(rozmiar_macierzy)] for i in range(rozmiar_macierzy)]

        for i in range(len(wiadomość)):
            wiersz = i // rozmiar_macierzy
            kolumna = i % rozmiar_macierzy
            if wiadomość[i] != ' ':
                macierz[wiersz][kolumna] = wiadomość[i]

        for wiersz in macierz:
            print(wiersz)

        wiadomosc_zaszyfrowana = ''.join([''.join(kolumna) for kolumna in zip(*macierz)])
        print(wiadomosc_zaszyfrowana)

        self.lineEdit_2.setText(wiadomosc_zaszyfrowana)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Poli(QDialog):
    def __init__(self):
        super(Poli, self).__init__()
        loadUi("poli.ui", self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text().lower()
        wiadomość_zaszyfrowana = self.lineEdit_2.text()

        alfabet = 'abcdefghijklmnopqrstuvwxyz '
        klucz = "bcd"

        lista = []

        for i, znak in enumerate(wiadomość):
            if znak in alfabet:
                if znak == " ":
                    zmieniony_znak = " "
                else:
                    klucz_znak = klucz[i % len(klucz)]
                    przesuniecie = alfabet.index(klucz_znak)
                    przesuniecie_index = (alfabet.index(znak) + przesuniecie) % len(alfabet)
                    zmieniony_znak = alfabet[przesuniecie_index]
                lista.append(zmieniony_znak)
            else:
                print("Zły znak:", znak)

        wiadomość_zaszyfrowana = "".join(lista)

        print("klucz:", klucz)
        print("Zaszyfrowana wiadomość:", wiadomość_zaszyfrowana)

        self.lineEdit_2.setText(wiadomość_zaszyfrowana)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Base64(QDialog):
    def __init__(self):
        super(Base64, self).__init__()
        loadUi("base64.ui", self)
        self.wstecz.clicked.connect(self.wsteczfunction)
        self.plik1.clicked.connect(self.plik1function)
        self.plik2.clicked.connect(self.plik2function)

    def szyfrujfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def plik1function(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        # Otwieramy plik wejściowy w trybie odczytu binarnego
        with open(path, 'rb') as file:
            file_content = file.read()

        encoded_content = ""
        index = 0

        while index < len(file_content):
            # Pobieramy trzy bajty z pliku
            chunk = file_content[index:index + 3]

            # Zamieniamy bajty na liczby całkowite
            num1 = chunk[0] if len(chunk) > 0 else 0
            num2 = chunk[1] if len(chunk) > 1 else 0
            num3 = chunk[2] if len(chunk) > 2 else 0

            # Rozdzielamy te liczby na 6-bitowe sekcje i zamieniamy na indeksy znaków Base64
            index1 = num1 >> 2
            index2 = ((num1 & 3) << 4) | (num2 >> 4)
            index3 = ((num2 & 15) << 2) | (num3 >> 6)
            index4 = num3 & 63

            # Tworzymy ciąg znaków Base64 używając indeksów
            encoded_content += base64_chars[index1] + base64_chars[index2] + base64_chars[index3] + base64_chars[index4]

            index += 3

        # Dodajemy znaki "=" na końcu, jeśli liczba bajtów nie jest podzielna przez 3
        padding = len(file_content) % 3
        if padding == 1:
            encoded_content = encoded_content[:-2] + "=="
        elif padding == 2:
            encoded_content = encoded_content[:-1] + "="

        print(encoded_content)
        self.lineEdit_2.setText(encoded_content)

    def plik2function(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

        # Otwieramy plik wejściowy w trybie odczytu binarnego
        with open(path, 'rb') as file:
            file_content = file.read()

        encoded_content = ""
        index = 0

        while index < len(file_content):
            # Pobieramy trzy bajty z pliku
            chunk = file_content[index:index + 3]

            # Zamieniamy bajty na liczby całkowite
            num1 = chunk[0] if len(chunk) > 0 else 0
            num2 = chunk[1] if len(chunk) > 1 else 0
            num3 = chunk[2] if len(chunk) > 2 else 0

            # Rozdzielamy te liczby na 6-bitowe sekcje i zamieniamy na indeksy znaków Base64
            index1 = num1 >> 2
            index2 = ((num1 & 3) << 4) | (num2 >> 4)
            index3 = ((num2 & 15) << 2) | (num3 >> 6)
            index4 = num3 & 63

            # Tworzymy ciąg znaków Base64 używając indeksów
            encoded_content += base64_chars[index1] + base64_chars[index2] + base64_chars[index3] + base64_chars[index4]

            index += 3

        # Dodajemy znaki "=" na końcu, jeśli liczba bajtów nie jest podzielna przez 3
        padding = len(file_content) % 3
        if padding == 1:
            encoded_content = encoded_content[:-2] + "=="
        elif padding == 2:
            encoded_content = encoded_content[:-1] + "="

        print(encoded_content)
        self.lineEdit_2.setText(encoded_content)


class Hamming(QDialog):
    def __init__(self):
        super(Hamming, self).__init__()
        loadUi("hamming.ui", self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text()

        bity = ''.join(format(ord(char), '08b') for char in wiadomość)

        # Obliczamy ilość dodatkowych bitów parzystości (r)
        r = 0
        while 2 ** r < len(bity) + r + 1:
            r += 1

        # Tworzymy kod Hamminga o długości n + r, gdzie n to długość tekstu
        encoded = ['0'] * (len(bity) + r)
        j = 0

        for i in range(1, len(encoded) + 1):
            if i == 2 ** j:
                j += 1
            else:
                encoded[i - 1] = bity[i - j - 1]

        # Inicjalizujemy listę do przechowywania bitów parzystości
        parity_bits = ['0'] * r

        # Obliczamy bity parzystości
        for j in range(r):
            parity_bit = 0
            for i in range(2 ** j - 1, len(encoded), 2 ** (j + 1)):
                parity_bit ^= int(encoded[i])
            encoded[2 ** j - 1] = str(parity_bit)
            parity_bits[j] = str(parity_bit)

        encoded_text = ''.join(encoded)

        wynik = encoded_text, ''.join(parity_bits)

        wiadomość_zaszyfrowana = encoded_text
        bity_parzystości = parity_bits
        print(wiadomość_zaszyfrowana)
        print(bity_parzystości)
        self.lineEdit_2.setText(wiadomość_zaszyfrowana)
        self.lineEdit_3.setText(str(bity_parzystości))

        print(wynik)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class RSA(QDialog):
    def __init__(self):
        super(RSA, self).__init__()
        loadUi("rsa.ui", self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text()

        # Generowanie liczb pierwszych p i q
        p = q = 4
        while any(p % i == 0 for i in range(2, p)):
            p = random.randint(100, 300)
        while any(q % i == 0 for i in range(2, q)) or p == q:
            q = random.randint(100, 300)

        print("p =", p, ",q =", q)

        # Obliczanie n, phi, e i d
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(1, phi)
        while any((phi % e == 0, e % 2 == 0)):
            e = random.randint(1, phi)
        d = 0
        while (d * e) % phi != 1 or d == e:
            d = random.randint(1, phi)

        # Szyfrowanie wiadomości
        wiadomość_zaszyfrowana = [(ord(char) ** e) % n for char in wiadomość]
        wynik = str(''.join(map(lambda x: str(x), wiadomość_zaszyfrowana)))
        print("Zaszyfrowana wiadomość:", wynik)
        self.lineEdit_2.setText(wynik)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class RSA_plik(QDialog):
    def __init__(self):
        super(RSA_plik, self).__init__()
        loadUi("rsa_plik.ui", self)
        self.plik1.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)

        # Odczytujemy zawartość pliku
        with open(path, 'r') as f:
            wiadomosc = f.read()

        # Generowanie kluczy publicznego i prywatnego
        (public_key, private_key) = rsa.newkeys(512)

        # Szyfrowanie wiadomości
        encrypted_msg = []
        for i in range(0, len(wiadomosc), 53):  # 53 bajty to maksymalny rozmiar bloku dla klucza 512-bitowego
            block = wiadomosc[i:i + 53]
            encrypted_block = rsa.encrypt(block.encode(), public_key)
            encrypted_msg.append(encrypted_block)

        wynik = str(' '.join(str(int.from_bytes(block, byteorder='big')) for block in encrypted_msg))
        print("Zaszyfrowana wiadomość:", wynik)
        self.lineEdit_2.setText(str(wynik))

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class DES(QDialog):
    def __init__(self):
        super(DES,self).__init__()
        loadUi("des.ui",self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text().lower()

        key = "hardcode"

        # Tworzenie obiektu szyfrującego
        cipher = pyDes.des(key, pyDes.ECB)

        # Szyfrowanie wiadomości
        zaszyfrowana_wiadomość = cipher.encrypt(wiadomość, padmode=pyDes.PAD_PKCS5)

        # Wyświetlanie zaszyfrowanej wiadomości jako szesnastkowego ciągu znaków
        print("Zaszyfrowana wiadomość:", zaszyfrowana_wiadomość.hex())

        wynik = str(zaszyfrowana_wiadomość.hex())
        self.lineEdit_2.setText(wynik)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class RC4(QDialog):
    def __init__(self):
        super(RC4,self).__init__()
        loadUi("rc4.ui",self)
        self.szyfruj.clicked.connect(self.szyfrujfunction)
        self.wstecz.clicked.connect(self.wsteczfunction)

    def szyfrujfunction(self):
        wiadomość = self.lineEdit.text().lower()

        # Klucz RC4 (przykładowy klucz)
        key = "hardcode"

        # Inicjalizacja S-box
        s_box = list(range(256))
        j = 0

        # Inicjalizacja permutacji klucza w S-box
        for i in range(256):
            j = (j + s_box[i] + ord(key[i % len(key)])) % 256
            s_box[i], s_box[j] = s_box[j], s_box[i]

        # Inicjalizacja wskaźników i szyfrowanie
        i = 0
        j = 0
        cipher_text = []

        for char in wiadomość:
            i = (i + 1) % 256
            j = (j + s_box[i]) % 256
            s_box[i], s_box[j] = s_box[j], s_box[i]
            k = s_box[(s_box[i] + s_box[j]) % 256]
            cipher_byte = ord(char) ^ k
            cipher_text.append(str(cipher_byte))

        wynik = str(' '.join(cipher_text))
        self.lineEdit_2.setText(wynik)

    def wsteczfunction(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app=QApplication(sys.argv)
mainwindow=Menu()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()
app.exec_()

