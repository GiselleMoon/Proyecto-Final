# Programa: Nomina.py
# Objetivo: Programa que define cuentas de nómina a partir de una cuenta por herencia.
# Autor: Binary Balance
# Fecha: 23/05/24

import Cuenta as c

class Nomina(c.Cuenta):
    def __init__(self, nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                 fecha_deposito, sucursal, estado, correo, telefono, rfc_empresa, nombre_empresa):
        """
        Constructor de una cuenta de débito.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_cuenta: Numero de la cuenta del cliente.
        :param float saldo: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_deposito: Fecha de pago de la cuenta de crédito con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        :param str rfc_empresa: RFC de la empresa.
        :param str nombre_empresa: Nombre de la empresa.
        """
        super().__init__(nombre_cliente, numero_cliente, numero_cuenta, saldo, fecha_apertura,
                         fecha_deposito, sucursal, estado, correo, telefono)

        self.__rfc_empresa = rfc_empresa
        self.__nombre_empresa = nombre_empresa


    #GETTERS
    @property
    def rfc_empresa(self):
        """
        Método para obtener el RFC de la empresa
        :return: RFC de la empresa.
        :rtype: str
        """
        return self.__rfc_empresa

    @property
    def nombre_empresa(self):
        """
        Método para obtener el nombre de la empresa.
        :return: Nombre de la empresa.
        :rtype: str
        """
        return self.__nombre_empresa

    #SETTERS
    @rfc_empresa.setter
    def rfc_empresa(self, rfc_empresa: str):
        """
        Método que permite establecer el RFC de la empresa.
        :param rfc_empresa: RFC de la empresa.
        """
        self.__rfc_empresa = rfc_empresa

    @nombre_empresa.setter
    def nombre_empresa(self, nombre_empresa:str):
        """
        Método que permite establecer el nombre de la empresa.
        :param nombre_empresa: Nombre de la empresa
        """
        self.__nombre_empresa = nombre_empresa



    def __str__(self):
        """
        Método para imprimir una cuenta de débito en formato cadena.
        :return: Una cuenta de débito en formato cadena.
        :rtype: str
        """
        return super().__str__().replace("CUENTA", "CUENTA NÓMINA").replace("producto", "cuenta").replace("Monto", "Saldo").replace("acción", "depósito") + \
            "RFC de la empresa: {} \nNombre de la empresa: {}\n".format(self.__rfc_empresa, self.__nombre_empresa)


    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta de nómina.
        :return: Representación iterable de una cuenta de nómina.
        :rtype: iterable
        """
        return iter(["Nómina", super().nombre_cliente, super().numero_cliente, super().numero_producto,
                     super().monto, super().fecha_apertura, super().fecha_accion, super().sucursal,
                     super().estado, super().correo, super().estado], self.__rfc_empresa, self.__nombre_empresa)


if __name__ == "__main__":
    nomina = Nomina("Vittorino Bianco", "000004", "12345694",
                    250000, "07-03-2023", "10-03-2023", 2, "Ciudad de México",
                    "vittorinocic@gmail.com", "5585471216", "DXIA050307ME1", "Desolé")

    print(nomina)
