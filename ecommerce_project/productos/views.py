from django.shortcuts import render
from productos.models import productos

def create_product(request):
    new_product = productos.objects.create(
        name="Teclado Mecanico Rex Dragon",
        price=35,
        descreption="""
        Es gamer: Sí
        //
        Idioma: Inglés US
        //
        Color de la retroiluminación: RGB
        //
        Tipo de switch: Outemu Brown
        //
        Con Bluetooth: Sí

        """)
    
    new_product1 = productos.objects.create(
        name="Monitor Tedge MNT24/01 led 24'' negro 220V",
        price=185,
        descreption="""
        Tamaño de la pantalla: 24 "
        //
        Con pantalla táctil: No
        //
        Con altavoces incorporados: Sí
        //
        Tipo de resolución: Full HD
        //
        Es reclinable: Sí
        //
        """)
    
    new_product2 = productos.objects.create(
        name="Silla de escritorio Smart Tech WS8511 gamer ergonómica  ",
        price=242,
        descreption="""
        Es gamer: Sí
        //
        Con altura regulable: Sí
        //
        Con respaldo reclinable: Sí
        //
        Es ergonómica: Sí
        //
        Con apoyabrazos ajustable: Sí
        //
        Es giratoria: Sí
        //
        
        
        """    )
    new_product3 = productos.objects.create(
        name="Placa de video Nvidia Colorful GeForce 10 Series GTX 1050 Ti 4GB",
        price=180,
        descreption="""
        Fabricante: Nvidia
        //
        Tipo de memoria gráfica: GDDR5
        //
        Interfaz con la placa madre: PCI-Express 3.0
        //
        Tamaño de memoria: 4 GB
        //
        Contectividad: DVI, HDMI, DisplayPort
        //
        """
        )
    new_product4 = productos.objects.create(
        name="Logitech G Series Lightspeed G305 blue",
        price=23,
        descreption=""""
        Tipo de mouse: De juego
        //
        Resolución del sensor: 12000 dpi
        //
        Tipo de sensor: Óptico
        //
        """
        )
        
    context = {
        "new_product":new_product,
        "new_product1":new_product1,
        "new_product2":new_product2,
        "new_product3":new_product3,
        "new_product4":new_product4
        

    }    
    return render(request, "new_product.html", context=context)

