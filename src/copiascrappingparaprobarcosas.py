from urllib.request import urlopen

url = "https://bertavr.github.io/Proyecto_Rick_y_Morty/basic.html"
page = urlopen(url)
html_bytes = page.read()
html_link = html_bytes.decode("utf-8")

def crear_caracteristicas(html):
    caracteristicas_dicc= {}
    caracteristica_añadir = False
    for marca in html:
        if marca == '"caracterstica">':
            caracteristica_añadir = True
        elif marca == "</li>":
            caracteristica_añadir = False
        if caracteristica_añadir== True:
            carcteriticas_dicc[nombre] = marca
        return caracteristicas_dicc
        print (crear_caracteristicas(html_link))

    