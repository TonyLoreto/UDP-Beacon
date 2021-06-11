#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

import socket
import sys
import re
import select

UDP_IP="0.0.0.0" # Recibir de cualquier cliente
#print("Ingresa el puerto XXXXX")
#UDP_PORT= int(input()) 
UDP_PORT0 = 1111#Enviar a
UDP_PORT1 = 1112#Recibir de
UDP_HOST0 = "192.168.50.56"#Enviar a
UDP_HOST1 = "192.168.1.100"#Recibir de
print ("Conectar/Enviar a %s" % UDP_HOST0)
print ("Conectar/Recibir de %s" % UDP_HOST1)

#Socket envio
sock0 = socket.socket( socket.AF_INET, # Internet
socket.SOCK_DGRAM ) # UDP

sock0.bind( (UDP_IP,UDP_PORT0) )

#Socket regreso
sock1 = socket.socket( socket.AF_INET, # Internet
socket.SOCK_DGRAM ) # UDP

sock1.bind( (UDP_IP,UDP_PORT1) )

# Pone el socket en modo de no bloqueo,
# evitando poner a recv en bucle infinito si no hay datos en el buffer
sock0.setblocking(0)
print("%s:%s Conexion establecida" %(UDP_HOST0, UDP_PORT0))
# print("Ingresa tu mensaje")


sock1.setblocking(0)
# print("Estableciendo la conexion...")
sock1.sendto(b"Starting socket UDP", (UDP_HOST1, UDP_PORT1))
print("%s:%s Conexion establecida" %(UDP_HOST1, UDP_PORT1))

while True:

    #Enviar mensaje 
    # Valida si se recibe captura desde el teclado
    HayDatosTeclado = select.select([sys.stdin],[],[],1)
    if HayDatosTeclado[0]:
        mensaje = sys.stdin.readline()
        print("Mensaje para remoto:", mensaje)
        sock0.sendto(mensaje.encode('utf8'), (UDP_HOST0, UDP_PORT0))
        # Valida si recibe algo por el socket
    # HayDatosSocket = select.select([sock0],[],[],0.5)
    # if HayDatosSocket[0]:
        # Socketdata = sock0.recv( 1024 ) # buffer size is 1024 bytes 
        # pass
        # HayDatosTeclado = []
        # HayDatosSocket = []

    #Recibir mensaje
    # Valida si recibe algo por el socket
    HayDatosSocket = select.select([sock1],[],[],0.5)
    if HayDatosSocket[0]:
        Socketdata = sock1.recv( 1024 ) # Buffer de 1024 bytes de tamao 
        sock0.sendto(Socketdata.encode('utf8'), (UDP_HOST0, UDP_PORT0))
        print ("Mensaje recibido: ", Socketdata)
        HayDatosTeclado = []
        HayDatosSocket = []
