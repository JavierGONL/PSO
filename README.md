# Hola, bienvenidos a nuestro repositorio

<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

## diagrama de clase particle
```mermaid
classDiagram
    class Particle{
        p_position
        speed
        value
        p_best_value
        p_best_position
        historial_positions
        initialize
        dimension
        initialize_particle()
        calculate_value()
    }
```
Cosas pendientes por hacer:
* optimizar codigo y hacerlo presentable


## diagrama de clase vector

```mermaid
classDiagram
direction TB
      class Point {
      + x
      + y
      + comp_to_list
      + __add__()
      + __radd__()
      + __sub__()
      + __rsub__()
      + __mul__()
      + __rmul__()
      + __str__()
      + __pow__()
      + __round__()
    }

    class Vector {
      + magnitud
      + calculate_magnitud()
      + get_direction()
      + __add__()
      + __rsub__()
      + __sub__()
      + __mul__()
      + __pow__()
      + __round__()
      + __str__()
    }

    Point <|-- Vector
```


Cosas pendientes por hacer:
* dormir bien
* hacer que los enjambres puedan recibir diferentes funciones
* hacer que los enjambres devuelvan las listas X,Y,Z para gráficar
* Crear la clase de gráfica
* revisar si matplotlib puede 

## diagrama de clase graficar

```mermaid
---
title: clase gráfica
---
classDiagram
    note "como hacer que las gráficas no sean un copypaste"
    class gráfica{
        +lista_x
        +lista_y
        +lista_z
        +addsubplot() -> gráfica 3D
        +Scatter() -> gráfica de puntos
        +cambiar_ventana() 

        }
```
