import 'dart:math';

void main() {
  List<int> lista1 = List.generate(7, (index) => Random().nextInt(71) + 30);
  List<int> lista2 = List.generate(7, (index) => Random().nextInt(71) + 30);
  List<int> lista3 = List.generate(7, (index) => Random().nextInt(71) + 30);
  print("Lista 1 generada de forma aleatoria: $lista1");
  print("Lista 2 generada de forma aleatoria: $lista2");
  print("Lista 3 generada de forma aleatoria: $lista3");

//double representa los datos en decimal
//para el promedio se calcula sumando todos los elementos de una lista
//y dividiendo el resultado entre el número de elementos en la lista.
//usamos el método reduce para sumar todos los elementos de la lista.
//luego se divide el resultado entre la longitud de la lista.
  double promedio1 = lista1.reduce((a, b) => a + b) / lista1.length;
  double promedio2 = lista2.reduce((a, b) => a + b) / lista2.length;
  double promedio3 = lista3.reduce((a, b) => a + b) / lista3.length;

  List<double> promedios = [promedio1, promedio2, promedio3];

  print("Promedios obtenidos: $promedios");
}
//integrantes: Alex Hernandez, Ignacio Soto, Nicolas Almuna
