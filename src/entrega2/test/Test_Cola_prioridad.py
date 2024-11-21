'''
Created on 29 oct 2024

@author: noelia
'''

from entrega2.tipos.Cola_de_prioridad import ColaDePrioridad

def test_cola_prioridad():
    cola=ColaDePrioridad()
    
    # Agregar pacientes
    cola.add("Paciente A", 3)
    cola.add("Paciente B", 2)
    cola.add("Paciente C", 1)
    
    # Verificar el espado de la cola
    assert cola.elements==['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."
    
    # Atender a los pacientes y verificar el orden de atención
    atención=[]
    while not cola.is_empty:
        atención.append(cola.remove())
        
    assert atención==['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    
    print("Pruebas superadas exitosamente")
    

if __name__ == '__main__':
    test_cola_prioridad()