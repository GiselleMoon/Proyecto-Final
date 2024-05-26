# Programa: Credito.py
# Objetivo: Programa que define cuentas de crédito a partir de una cuenta por herencia.
# Autor: Binary Balance
# Fecha: 23/05/24

import Cuenta as c
from datetime import date
from datetime import datetime

class Credito(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_tarjeta, importe, fecha_apertura,
                 fecha_pago, sucursal, estado, correo, telefono, monto_usado, fecha_vencimiento):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_tarjeta: Numero de tarjeta del cliente.
        :param float importe:c Cantidad de dinero del crédito de la tarjeta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_pago: Fecha de pago de la cuenta de crédito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        :param float monto_usado: Monto del crédito usado.
        :param str fecha_vencimiento:
        """
        super().__init__(nombre_cliente, numero_cliente, numero_tarjeta, importe, fecha_apertura,
                         fecha_pago, sucursal, estado, correo, telefono)

        self.__monto_usado = monto_usado

        try:
            self.__fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: {} no está en el formato dd-mm-yyyy".format(self.__fecha_vencimiento))

    #GETTERS
    @property
    def monto_usado(self):
        """
        Método para obtener el monto usado del importe del crédito.
        :return: Monto usado del crédito.
        :rtype: float
        """
        return self.__monto_usado

    @property
    def fecha_vencimiento(self):
        """
        Método para obtener la fecha de vencimiento de la tarjeta.
        :return: Fecha de vencimiento de la tarjeta.
        :rtype: datetime.date
        """
        return self.__fecha_vencimiento

    #SETTERS
    @monto_usado.setter
    def monto_usado(self, monto_usado: float):
        """
        Método que permite establecer el monto usado del crédito.
        :param float monto_usado: Monto usado del crédito.
        """
        self.__monto_usado = monto_usado

    @fecha_vencimiento.setter
    def fecha_vencimiento(self, fecha_vencimiento:str):
        """
        Método que permite establecer la fecha de vencimiento de la tarjeta.
        :param fecha_vencimiento: Fecha de vencimiento de la tarjeta.
        """
        try:
            self.__fecha_vencimiento = datetime.strptime(self.__fecha_vencimiento, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: {} no está en el formato dd-mm-yyyy".format(self.__fecha_vencimiento))



    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("CUENTA", "CUENTA CRÉDITO").replace("producto", "tarjeta").replace("Monto", "Importe").replace("acción", "pago") + \
            "\nMonto usado del crédito: {} \nFecha de vencimiento de la tarjeta: {}\n".format(self.__monto_usado, self.__fecha_vencimiento.strftime("%d-%m-%Y"))


    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de crédito.
        :return: Representación iterable de una cuenta de crédito.
        :rtype: iterable
        """
        return iter(["Crédito", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado], self.__monto_usado, self.__fecha_vencimiento)


if __name__ == "__main__":
    credito = Credito("Michael Vázquez Esparza", "000003", "12345681",
                    250000, "07-03-2023", "10-03-2023", 2, "Ciudad de México",
                    "michavaz@gmail.com", "5512164325", 80000, "15-06-2026")

    print(credito)
