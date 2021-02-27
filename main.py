import json
import matplotlib.pyplot as plot
from os import path
from scapy.layers.inet import IP, TCP, UDP
from tkinter import Tk, Label, Entry, StringVar, Button

from capture import Capture
from package import Package

# Fereastra principala - Initializare si Setare Parametri
root_window = Tk()
root_window.title("Operations with Captures")
root_window.geometry('500x500')
root_window.configure(background='light blue')

# Titlul aplicatiei
title = Label(text='Python Professional Final Project',
              font=('Helvetica', 14, 'bold'))
title.pack()

# Autorul aplicatiei
author = Label(text='Ionut-Eduard Paunoiu',
               font=('Helvetica', 12))
author.pack()

# Introducerea filtrului de catre utiizator
filter_name = StringVar()  # Pentru a putea fi utilizat de catre Entry
filter_name.set('')  # Il setam null initial

filter_label = Label(root_window, text="1. Please introduce a filter:",
                     font=('Helvetica', 12, 'bold'))
filter_label.pack()

filter_entry = Entry(root_window, textvariable=filter_name)
filter_entry.pack()

# Captura pe toate interfetele de retea
capture = Capture()  # Instanta (Singleton) clasei Capture
packages_list = []  # Lista de pachete necesara aplicatiei


# Functia efectiva de capturare a pachetelor.
def start_capturing():
    packages_list.clear()  # In cazul in care utilizatorul alege un alt filtru, o sa golim lista existenta de pachete
    packages = capture.sniff_packages(filter_name.get())  # Faceam capturarea
    if filter_name.get() == '':  # Verificam daca utilizatorul a introdus sau nu un filtru
        print('You haven\'t introduced any filter. The sniffing was done without filters.')
    else:
        print("The introduced filter was: " + filter_name.get())
    for package in packages:
        # Pentru fiecare pachet din cele capturate, vom initializa cate un obiect de tip Package
        # si ii vom atribui atributele aferente in cazul in care le are.
        p = Package()
        p.Ethernet_src = package['Ethernet'].src
        p.Ethernet_dst = package['Ethernet'].dst
        if package.haslayer(IP):
            p.IP_src = package['IP'].src
            p.IP_dst = package['IP'].dst
            p.IP_version = package['IP'].version
            p.IP_protocol = package['IP'].proto
        if package.haslayer(UDP):
            p.UDP_sport = package['UDP'].sport
            p.UDP_dport = package['UDP'].dport
        if package.haslayer(TCP):
            p.TCP_sport = package['TCP'].sport
            p.TCP_dport = package['TCP'].dport
        # Adaugam pachetul in lista de pachete si il afisam la consola.
        packages_list.append(p)
        print(p.get_string())
    print("--------------------------------------------------------------------------------")
    filter_name.set('')


# Buton care incepe capturarea efectiva, conform functiei start_capturing().
filter_button = Button(root_window,
                       text='Capture some packages',
                       font='Helvetica',
                       command=start_capturing)

filter_button.pack()

# Introducerea caii catre fisierul
path_name = StringVar()
path_name.set('')

path_label = Label(root_window, text="2. Please introduce the path:",
                   font=('Helvetica', 12, 'bold'))
path_label.pack()

path_entry = Entry(root_window, textvariable=path_name)
path_entry.pack()


# Salvarea efectiva ca JSON
def create_json():
    with open(path_name.get(), 'a+') as json_file:  # Deschide sau creeaza fisierul in caz ca nu exista
        # Scriem in fisierul de output datele referitoare la fiecare pachet, in format JSON.
        for package in packages_list:
            json.dump(package.get_string(), json_file, sort_keys=True, indent=4)
            json_file.write("\n")
    # Daca fisierul exista, afisam un mesaj corespunzator.
    if path.exists(path_name.get()):
        print('JSON saved successfully!')
    else:
        print('Couldn\'t save JSON!')
    path_name.set('')


# Butonul care creeaza efectiv fisierul final, conform functiei create_json()
path_button = Button(root_window,
                     text='Save as JSON',
                     font='Helvetica',
                     command=create_json)

path_button.pack()

# Statistici
statistics_label = Label(root_window, text="3. Display a PieChart",
                         font=('Helvetica', 12, 'bold'))
statistics_label.pack()


# Afisarea piechart-ului
def show_piechart():
    no_tcp = 0
    no_udp = 0
    # Calculam numarul de pachete TCP si respectiv UDP.
    for package in packages_list:
        if package.is_tcp():
            no_tcp += 1
        elif package.is_udp():
            no_udp += 1
    # Crearea efectiva a piechart-ului, conform cursului.
    pie_slices = [no_tcp, no_udp]
    labels = ['TCP Packages', 'UDP Packages']
    plot.pie(pie_slices, labels=labels, colors=['c', 'm', 'r', 'b'], startangle=90, shadow=True, autopct='%.1f%%')
    plot.title('Distribution of TCP/UDP packages')
    plot.show()


# Butonul care afiseaza piechar-ul corespunzator.
statistics_button = Button(root_window,
                           text='Show statistics',
                           font='Helvetica',
                           command=show_piechart)
statistics_button.pack()

# Pornim event loop-ul tkinter care afiseaza si fereastra.
root_window.mainloop()
