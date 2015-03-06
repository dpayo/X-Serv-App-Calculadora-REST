#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Ejercicio Calculadora REST
 /sumar /restar /mult /div
"""
import webapp
import sys
import socket

class Calc_rest(webapp.webApp):
    def operate (self,operador,op1,op2):
        if operador == '+':
            result = op1+op2
        elif operador == "-":
            result = op1-op2
        elif operador == "*":
            result = op1 *op2
        else:
            result = op1/op2
        return result
        
    def parse(self, request):
        """Parse the received request, extracting the relevant information."""
        verb= request.split()[0]
        recurso = request.split()[1]
        body = request.split('\r\n\r\n')[1]
        return (verb,body,recurso)
        
    def process(self, (verb,body,recurso)):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
       
        if verb == "GET":
            try:
                print recurso
                (code, message) = ("200 Ok",str(self.op1)+str(self.operador)+str(self.op2)+'='+str(self.result))
                
            except:
                (code, message) = ("404","Not Found")
        elif verb == "PUT":
             self.operador= body[1]
             self.op1=float(body[0])
             self.op2=float(body[2])
             self.result = self.operate (self.operador,self.op1,self.op2)
             (code, message) = ("200 Ok",'Actualizando...'+str(body))   
            
        return (code,message)
if __name__ == "__main__":
    try:
        testCalc = Calc_rest('localhost', 1234)
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
        sys.exit()
