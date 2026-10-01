from datetime import date

class ProductoKwikE:
   def __init__ (self,descripcion,id_producto,fecha_vencimiento,precio,stock):
       self.descripcion = descripcion
       self.id_producto = id_producto
       self.fecha_vencimiento = fecha_vencimiento
       self.precio = precio
       self.stock = stock
         
   def actualizar_producto(self,descripcion=None,precio=None,stock=None):
       if descripcion is not None:
          self.descripcion=descripcion
       if precio is not None:
          self.precio=precio
       if stock is not None:
          self.stock=stock

   def dias_para_expirar(self):
       hoy = date.today()
       dias_rest=(self.fecha_vencimiento-hoy).days
    
       if dias_rest < 0:
       print("El producto",self.descripcion,"ha expirado")
          self.stock = 0
       return dias_rest
    
   def __str__ (self):
       return "Producto:" + self.descripcion +"-ID:" + str(self.id_producto) + "-Precio:$" + str(self.precio) + "-Stock:" + str(self.stock)
   
   def __eq__ (self,otro):
       if self.id_producto == otro.id_producto and self.descripcion == otro.descripcion:
          return True
       else:
          return False