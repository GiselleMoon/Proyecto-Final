#Programa: Debito.py
#Objetivo: Programa que define cuentas de débito a partir de una cuenta por herencia.
#Autor: Binary Balance
#Fecha: 23/05/24

import Cuenta as c

class Debito(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_corte, sucursal, estado, correo, telefono):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_cuenta: Número de cuenta del cliente.
        :param float saldo: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_corte: Fecha de corte de la cuenta de débito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        """
        super().__init__(nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_corte, sucursal, estado, correo, telefono)

    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("CUENTA", "CUENTA DÉBITO").replace("producto", "cuenta").replace("Monto", "Saldo").replace("acción", "corte")

    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de débito.
        :return: Representación iterable de una cuenta de débito.
        :rtype: iterable
        """
        return iter(["Débito", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado])


if __name__ == "__main__":
    debito = Debito("Louisa Martínez López", "000002", "1234",
                    60000, "23-02-2023", "27-03-2023", 2, "Ciudad de México",
                    "loumarp@gmail.com", "5587926947")

    print(debito)
