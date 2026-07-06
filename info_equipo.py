nombre = input("Introduce tu nombre: ")
pais = input("Introduce tu pais: ")
descripcion = input("Explicate en una breve descripcion: ")

def presentar(mi_nombre,mi_pais,mi_descripcion):
            print("El usuario " 
                + str(mi_nombre) + " vieve en " + str(mi_pais) + ", se describio a si mismo como: "
                + str(mi_descripcion))
            return
presentar(nombre,pais,descripcion)

#ejemplos
presentar("Juan","Bolivia ","Amable con ganas de trabajar")
presentar("Alicia","Francia","En un futuro sere una gran pintora")