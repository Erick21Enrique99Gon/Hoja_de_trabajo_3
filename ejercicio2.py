def ingresoNumero():
    numeroIngresado = int (input('Escriba un numero entre 1 y 10 \n'))
    ruta = 'C:\\Users\\González Chávez\\Documents\\erick\\python\\HOJADETRANAJO\\Hoja_de_trabajo_3\\Tabla'+str(numeroIngresado)+'.txt'
    tabla = [
            numeroIngresado*0,
            numeroIngresado*1,
            numeroIngresado*2,
            numeroIngresado*3,
            numeroIngresado*4,
            numeroIngresado*5,
            numeroIngresado*6,
            numeroIngresado*7,
            numeroIngresado*7,
            numeroIngresado*8,
            numeroIngresado*9,
            numeroIngresado*10,
            ]
    if 1<= numeroIngresado <=10:
        archivo = open(ruta,'a+')
        for i in tabla:
                archivo.write(str(i)+'\n')
        
        archivo.close
        

ingresoNumero()