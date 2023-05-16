import 'dart:math';

void main(){
 
  List<int> lista1 = [3,4,7,9,8,5,1,2,5,7];
  

  List<int> lista2 = List.generate(10, (index)=> Random().nextInt(5)-5);


  List<int> lista3 = [];
  for (int i = 0; i < 10; i++) {
    lista3.add(lista1[i] + lista2[i]);
  }
    print(lista3) 
}














