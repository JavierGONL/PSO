<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>
# diagrama vector 

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