//Testing for equality
import "dart:io";

void main() {
  print('Enter a random number: ');
  int num1 = int.parse(stdin.readLineSync()!);
  bool doesOneEqualTwo = (1 == num1);
  print('Is 1 equivalent to ${num1}? ${doesOneEqualTwo}');

  print('Enter your score: ');
  int score = int.parse(stdin.readLineSync()!);
  var message = (score > 60) ? 'You Passed' : 'You failed';
  print(message);
}
