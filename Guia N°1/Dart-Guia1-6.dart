import 'dart:math';

void main() {
  List<int> a = [4, 3, 2, 2, 1];
  List<int> b = [-3, 2, 8, 0, 1];

//para la multiplicacion de a y b
  List<int> c = List.generate(a.length, (index) => a[index] * b[index]);
  print("Multipliacion de la lista a y b: $c");

//generamos una nueva lista random "c"
  List<int> randomList = List.generate(5, (index) => -Random().nextInt(5) - 1);

//Concatenamos la lista "c" con la lista random creada
  c.addAll(randomList);
  print("Lista concatenada con 5 elementos aleatorios : $c");

//usamos sort para comparar elementos de la lista para determinar su orden en este caso "x" e "y"
//la funcion usa el metodo compareTo para comparar los dos elementos
//utilizamos y.compareTo(x) en lugar de x.compareTo(y), invierte el orden de comparación
//lo que hace que la lista se ordene en orden descendente en lugar de ascendente.
  c.sort((x, y) => y.compareTo(x));
  print("Lista ordenada de forma descendente: $c");
}
//integrantes: Alex Hernandez, Ignacio Soto, Nicolas Almuna
