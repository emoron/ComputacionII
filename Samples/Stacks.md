<ol>
<li> Un banco tiene guardados los registros de los movimientos en una lista.   Los movimientos están ordenados primero por fecha y luego por numero de cuenta.

El tipo del elemento de la lista es:

```
 TElemLista Fecha  Nro_Cta Monto Tipo (Deposito/Extracción)
```

Realizar procedimientos para este TDA que:  

*  Permita Calcular la cantidad de depositos realizados entre el 01/01/2004 y el 31/07/2004.
*  Permita Calcular el total depositado y extraído en el año 2003.
*  Permita Calcular el saldo de la cuenta 8894 del año 2003.  

</li>

<li> Una empresa de servicios guarda es una pila, las tareas que debe realizar cada empleado.
La estructura es la siguiente:

  - Código Empleado
  - Cantidad de Tareas
  - Pila de Tareas

 La Pila de Tareas  

  * Area Solicitante
  * Descripción

Realizar funciones para este TDA que:
  - Permita Ingresar una nueva tarea en el empleado que tenga menos tareas.
  - Permita Procesar las tareas de los empleados 15 a 30, sacándolas de la pila.

</li>

<li>Un supermercado decidió crear un sistema para poder remarcar sus precios por lo tanto creo un TDA el cual llamaron **“PRODUCTOS_REMARCADOS”**. Dicho TDA esta compuesto por:

* Fecha Actualizacion (Ultima actualización de precios)
* lista de productos:
    * cod_producto (Clave de Ordenamiento)
    * precio
    * cantidad de remarcaciones efectuadas
* Cola de precios anteriores:
     * fecha_actualizacion
     * precio

Dada la estructura **“PRODUCTOS_REMARCADOS”** se pide:

*  Definir el TDA **“PRODUCTOS_REMARCADOS”** y cada uno de los tipo utilizados para el
mismo implementadolo con punteros.
*  Desarrollar la primitiva de este TDA llamada “productos mas remarcados” que recibe
como parámetro una variable del TDA **PRODUCTOS_REMARCADOS**, y devuelve una
lista con los productos que fueron remarcados mas de N (parámetro del procedimiento)
veces.

La lista contendrá el código de producto (la lista se mantiene ordenada por este
campo), la cantidad de veces que sufrió remarcacion y el promedio de los precios
anteriores.   

</li>

<li>Un Hospital desarrollo un sistema de Turnos, el cual se implemento con un TDA el cual
denominaron **“AGENDAS_MEDICAS”**. El mismo tiene dos fechas que indican desde cuando y
hasta cuando están programados los turnos para dar, el nombre de la especialidad de esa agenda y una lista_simple.

Este TDA **”AGENDAS MEDICAS”** posee en cada uno de los elementos de la lista simple.

```python
(Codigo_medico (la lista esta ordenada por este campo), Fecha de atención,
cantidad_turnos_libres y cantidad_turnos ocupados)
```

Dado el TDA **“AGENDAS_MEDICAS”** se pide:

- Definir el TDA **“AGENDAS_MEDICAS”** y cada uno de los tipo utilizados para el mismo
implementado con punteros las listas que se requieran.

-  Desarrollar la primitiva de este TDA llamada “Verificar_turno” que recibe como
parámetro el TDA agenda, un codigo de medico y una fecha y devuelve una variable
booleana en true si hay disponibilidad de turnos en esa fecha para ese medico.

</li>
</ol>
