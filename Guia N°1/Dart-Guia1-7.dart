void main() {
  List<dynamic> lista = ["a", 2, 0, "b", 8, "c"];

//creamos una lista vacia para los numeros de la lista original
  List<int> numeros = [];

//usamos un bucle para recorrer la lista
//con la condicion if verificamos si el elemento es un numero entero "int"
//si el elemento es entero se agrega a la lista "numeros" utilizando el metodo "add"
  for (var element in lista) {
    //var permite declarar variables sin tener que especificar su tipo
    if (element is int) {
      numeros.add(element);
    }
  }
  print("La lista omitiendo los caracteres: $numeros");
}

//integrantes: Alex Hernandez, Ignacio Soto, Nicolas Almuna