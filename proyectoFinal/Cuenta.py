#Programa: Cuenta.py
#Objetivo: Programa que define una clase para manejar cuentas.
#Autor: Binary Balance
#Fecha: 23/05/24


from datetime import date
from datetime import datetime
from email_validator import validate_email, EmailNotValidError

class Cuenta:
    def __init__(self, nombre_cliente, numero_cliente, numero_producto, monto, fecha_apertura,
                 fecha_accion, sucursal, estado, correo, telefono):
        """
        Constructor de una cuenta base.
        :param str nombre_cliente: El nombre del cliente.
        :param str numero_cliente: El número de cliente.
        :param str numero_producto: Número del producto contratado por el cliente.
        :param float monto: Cantidad de dinero en la cuenta.
        :param str fecha_apertura: Fecha de apertura de la cuenta con formato dd-mm-yyyy.
        :param str fecha_accion: Fecha en la que la cuenta recibe una acción con formato dd-mm-yyyy.
        :param int sucursal: Número de sucursal.
        :param str estado: Nombre del estado de la República donde se encuentra la sucursal.
        :param str correo: Dirección de correo electrónico del cliente.
        :param str telefono: Número de teléfono del cliente.
        """
        
        self.__nombre_cliente = nombre_cliente
        self.__numero_cliente = numero_cliente
        self.__numero_producto = numero_producto
        self.__monto = monto
        
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha de apertura ingresada: {} no está en el formato dd-mm-yyyy\n".format(fecha_apertura))
            
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: {} no está en el formato dd-mm-yyyy\n".format(fecha_accion))

        self.__sucursal = sucursal
        self.__estado = estado

        try:
            self.__correo = validate_email(correo).email
        except EmailNotValidError:
            print("El correo ingresado: {} no tiene un formato válido\n".format(correo))

        self.__telefono = telefono


    #GETTERS
    @property
    def nombre_cliente(self):
        """
        Método para obtener el nombre completo del cliente.
        :return: Nombre completo del cliente.
        :rtype: str
        """
        return self.__nombre_cliente

    @property
    def numero_cliente(self):
        """
        Método para obtener el número de cliente.
        :return: Número de cliente.
        :rtype: str
        """
        return self.__numero_cliente

    @property
    def numero_producto(self):
        """
        Método para obtener el número del producto del cliente.
        :return: Número del producto.
        :rtype: str
        """
        return self.__numero_producto

    @property
    def monto(self):
        """
        Método para obtener el monto disponible en la cuenta.
        :return: Monto de dinero en la cuenta.
        :rtype: float
        """
        return self.__monto

    @property
    def fecha_apertura(self):
        """
        Método para obtener la fecha de apertura de la cuenta.
        :return: Fecha de apertura de la cuenta.
        :rtype: datetime.date
        """
        return self.__fecha_apertura

    @property
    def fecha_accion(self):
        """
        Método para obtener la fecha en la que la cuenta recibe una acción.
        :return: Fecha en la que la cuenta recibe una acción.
        :rtype: datetime.date
        """
        return self.__fecha_accion

    @property
    def sucursal(self):
        """
        Método para obtener el número de sucursal.
        :return: Número de sucursal.
        :rtype: int
        """
        return self.__sucursal

    @property
    def estado(self):
        """
        Método para obtener el estado de la República a la que pertenece la sucursal.
        :return: Estado de la República a la que pertenece la sucursal.
        :rtype: str
        """
        return self.__estado

    @property
    def correo(self):
        """
        Método para obtener el correo electrónico del cliente.
        :return: Correo electrónico del cliente.
        :rtype: str
        """
        return self.__correo

    @property
    def telefono(self:str):
        """
        Método para obtener el número de teléfono del cliente.
        :return: Número de telefono del cliente.
        :rtype: str
        """
        return self.__telefono

    #SETTERS
    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente:str):
        """
        Método que permite establecer el nombre del cliente.
        :param nombre_cliente: Nombre del cliente.
        """
        self.__nombre_cliente = nombre_cliente

    @numero_cliente.setter
    def numero_cliente(self, numero_cliente:str):
        """
        Método que permite establecer el número de cliente.
        :param numero_cliente: Número del cliente.
        """
        self.__numero_cliente = numero_cliente

    @numero_producto.setter
    def numero_producto(self, numero_producto:str):
        """
        Método que permite establecer el número del producto contratado por el cliente.
        :param numero_producto: Número del producto contratado por el cliente.
        """
        self.__numero_producto = numero_producto

    @monto.setter
    def monto(self, monto:float):
        """
        Método que permite establecer el monto de dinero en la cuenta.
        :param monto: Monto de dinero en la cuenta.
        """
        self.__monto = monto

    @fecha_apertura.setter
    def fecha_apertura(self, fecha_apertura:str):
        """
        Método que permite establecer la fecha de apertura de la cuenta.
        :param fecha_apertura: Fecha de apertura de la cuenta.
        """
        try:
            self.__fecha_apertura = datetime.strptime(fecha_apertura, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha de apertura ingresada: '{}' no está en el formato dd-mm-yyyy\n".format(fecha_apertura))
####################

    @fecha_accion.setter
    def fecha_accion(self, fecha_accion:str):
        """
        Método que permite establecer la fecha de la accion aplicada a la cuenta.
        :param fecha_accion: Fecha de la accion aplicada a la cuenta.
        """
        try:
            self.__fecha_accion = datetime.strptime(fecha_accion, "%d-%m-%Y").date()
        except ValueError:
            print("La fecha ingresada: '{}' no está en el formato dd-mm-yyyy\n".format(self.__fecha_accion))

    @sucursal.setter
    def sucursal(self, sucursal:int):
        """
        Método que permite establecer el número de sucursal a la que pertenece la cuenta.
        :param sucursal: El número de sucursal.
        """
        self.__sucursal = sucursal

    @estado.setter
    def estado(self, estado:str):
        """
        Método que permite establecer el estado de la República al cual pertenece la sucursal.
        :param estado: Estado de la República al cual pertenece la sucursal.
        """
        self.__estado = estado

    @correo.setter
    def correo(self, correo:str):
        """
        Método que permite establecer el correo electrónico del cliente.
        :param correo: Correo electrónico del cliente.
        """
        try:
            self.__correo = validate_email(correo)
        except EmailNotValidError:
            print("El correo ingresado: {} no tiene un formato válido\n".format(self.__correo))

    @telefono.setter
    def telefono(self, telefono:str):
        """
        Método que permite establecer el número de teléfono del cliente.
        :param telefono: Número de teléfono del cliente.
        """
        self.__telefono = telefono

    #Método STR
    def __str__(self):
        """
        Método para imprimir una cuenta como cadena.
        :return: La cuenta en formato cadena
        :rtype: str
        """
        return "|CUENTA|\nNombre del cliente: {}\nNúmero de cliente: {}\nNúmero de producto: {}\n"\
            "Monto: {}\nFecha de apertura: {}\nFecha de acción: {}\nSucursal: {}\n"\
            "Estado: {}\nCorreo: {}\nTeléfono: {}".format(self.__nombre_cliente,
                                                            self.__numero_cliente,
                                                            self.__numero_producto,
                                                            self.__monto,
                                                            self.__fecha_apertura.strftime("%d-%m-%Y"),
                                                            self.__fecha_accion.strftime("%d-%m-%Y"),
                                                            self.__sucursal,
                                                            self.__estado,
                                                            self.__correo,
                                                            self.__telefono)

    def __iter__(self):
        """
        Método para devolver una representación iterable de una cuenta.
        :return: Representación iterable de una cuenta.
        :rtype: iterable
        """
        return iter(["Cuenta", self.__nombre_cliente, self.__numero_cliente, self.__numero_producto,
                     self.__monto, self.__fecha_apertura, self.__fecha_accion, self.__sucursal,
                     self.__estado, self.__correo, self.__estado])

if __name__ == "__main__":
    cuenta = Cuenta("Luis Francisco Revuelta", "000001", "12345678",
                    100000, "15-04-2023", "25-05-2023", 4, "Ciudad de México",
                    "luisfrancis@gmail.com", "5534689876")
    print(cuenta)


        


