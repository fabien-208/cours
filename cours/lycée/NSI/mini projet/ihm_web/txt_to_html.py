#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
programme qui sert a trier les données de data.tsv
"""



def read_data(filename):
    """
    retourne les données du fichier tsv en liste
    filename = nom de fichier (string)
    """
    liste = []

    EOF = 0
    fichier = open(filename, encoding="UTF-8")
    while EOF != 1:
        ligne=fichier.readline()
        if ligne =="":
            EOF = 1
        else:
            ligneModifier = ligne.rstrip()
            ligneModifier2 = ligneModifier.split('\t')
            liste.append(ligneModifier2)
    
    return liste



def affiche_html(filename:str)->str:
    """
    retourne le code html des données
    data = liste des données(liste)
    """
    ofile = read_data(filename)
    headfile = open("ihm-web-statique.txt", encoding="UTF-8")
    head = headfile.readlines()

    html = ""
    for i in range(len(head)):
        html += head[i]
    html += "<body><table>"
    loop = 0
    for i in range(len(ofile)):
        if loop == 0:
            if i == 0:
                html += ligne2html(ofile[i], "th", 0)
            else:
                html += ligne2html(ofile[i], "td", 0)
            loop = 1
        else:
            if i == 0:
                html += ligne2html(ofile[i], "th", 1)
            else:
                html += ligne2html(ofile[i], "td", 1)
            loop = 0

    html += "</table></body></html>"
    #with open("test.html", "w" ,encoding="UTF-8") as data:
    #    data.write(html)
    return html
def ligne2html(ligne:list, typ, loop)->str:
    """
    convertie une ligne en code html

    >>> ligne2html(["a", "b", "c"], "td")
    '<tr><td>a</td><td>b</td><td>c</td></tr>'
    >>> ligne2html(["a", "b", "c"], "th")
    '<tr><th>a</th><th>b</th><th>c</th></tr>'
    >>> ligne2html(["bonsoir", "coucou", "test"], "th")
    '<tr><th>bonsoir</th><th>coucou</th><th>test</th></tr>'
    """
    
    if loop == 0:
        html = "<tr class = gray>"
        if typ == "td":
            for i in range(len(ligne)):
                html = html + "<td>{}</td>".format(ligne[i])
        else:
            for i in range(len(ligne)):
                html = html + "<th>{}</th>".format(ligne[i])
        html = html + "</tr>\n"
    else:
        html = "<tr>"
        if typ == "td":
            for i in range(len(ligne)):
                html = html + "<td>{}</td>".format(ligne[i])
        else:
            for i in range(len(ligne)):
                html = html + "<th>{}</th>".format(ligne[i])
        html = html + "</tr>\n"
    return html


if __name__ == __name__:
    import doctest
    #doctest.testmod(verbose=True)

import http.server

PORT = 8000
host = 'localhost'

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        html = bytes(affiche_html("data.tsv"), 'utf8')
        self.wfile.write(html)

def filtre(data, descrioteur, valeur):
    break

serveur = (host, PORT)
httpd = http.server.HTTPServer(serveur, SimpleHTTPRequestHandler)
print("serving at :", httpd.server_address)
httpd.serve_forever()
