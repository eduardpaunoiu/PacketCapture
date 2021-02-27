# PacketsCapture
Proiect Final Python Professional - Aplicatie Tkinter pentru capturarea unor pachete de retea

    Entry-point-ul aplicatiei mele este fisierul main.py care contine codul sursa al aplicatie tkinter in sine,
impreuna cu cele 3 cerinte implementate sub forma unor metode.
    Pentru inceput, am initializat cateva label-uri pentru titlu si autor, iar mai apoi m-am folosit de label-uri,
entry-uri si butoane pentru a implementa cerintele aplicatiei.
    In main am initializat un singur obiect de tip Capture si o lista de pachete, cu care voi opera de-a lungul programului.
    Din punct de vedere al utilizatorului, la primul subpunct, acesta trebuie sa introduca(dar nu obligatoriu) in entry
un nume de filtru. In cazul in care acesta nu specifica vreun filtru, se va face captura folosind folosind sniff() fara
parametrul filter. Apasarea butonului duce la apelarea metodei start_capturing(), care va initializa lista de pachete
si va afisa in consola continutul acestora in format JSON.
    Cel de-al doilea buton va facea parsarea tuturor informatiilor despre pachete (in format JSON) intr-un fisier dat
de utilizator, prin intermediul metodei create_json(). Fisierul poate sa existe sau nu, iar in caz negativ va fi creat
de catre program.
    Ultimul buton va duce la apelarea metodei show_piechart() si, evident, va afisa un PieChart ce reprezinta distributia
de pachete TCP si UDP, alaturi de procentele corespunzatoare.
