void main() {
  var andrewKim = Human();
  andrewKim.walking(); //INSTANCE METHOD
  print(andrewKim.skinColor); //INSTANCE VARIABLE
  print(Human.info); //CLASS VARIABLE
  Human.breathing(); //CLASS METHOD
}

class Human {
  String? name; //INSTANCE VARIABLE
  int? age; //INSTANCE VARIABLE
  String skinColor = "All colors are beautiful"; //INSTANCE VARIABLE

  static String info = "This is info of the class Human"; //CLASS VARIABLE

  //INSTANCE METHOD
  void walking() {
    print("Human is walking.");
  }

  //CLASS METHOD
  static void breathing() {
    print("Human is breathing.");
  }
}
