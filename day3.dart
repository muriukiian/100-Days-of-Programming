//control flow
import 'dart:io';

userInfo2() {
  print('Enter your full name: ');
  var name = stdin.readLineSync();
  print('Enter your phone number: ');
  var phoneNumber = stdin.readLineSync();
  print('Enter your ID or Passport number: ');
  var id = stdin.readLineSync();
  print('Enter your age: ');
  var age = stdin.readLineSync();
  print('Are you a christian? (True or False)');
  var isChristian = stdin.readLineSync();

  Map userInfo1 = {};
  userInfo1['name'] = name;
  userInfo1['phoneNumber'] = phoneNumber;
  userInfo1['I.D'] = id;
  userInfo1['age'] = age;
  userInfo1['isChristian'] = isChristian;

  return (userInfo1);
}

void main() {
  List countries = [
    'Kenya',
    'Uganda',
    'Tanzania',
    'Uruguay',
    'Republic of Korea',
    'China'
  ];
  int x = 0;
  while (x <= 5) {
    print(countries[x]);
    x++;
  }
  int y;
  for (y = 5; y >= 0; y--) {
    print(countries[y]);
  }
  int z;
  for (z = 2; z > 0; z--) {
    print(userInfo2());
  }
}
