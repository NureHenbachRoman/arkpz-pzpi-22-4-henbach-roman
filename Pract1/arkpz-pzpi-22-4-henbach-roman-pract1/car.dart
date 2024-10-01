class Car {
  String name;
  bool hasWheels = false;
  bool hasEngine = false;
  bool hasBody = false;
  
  Car(this.name);
  
  void assemble(){
    print('Starting assembly of ${name}');
    addBody();
    addEngine();
    addWheels();
    print('${name} is assembled');
  }
  
  void addBody() {
    hasBody = true;
    print('Body is attached.');
  }

  void addEngine() {
    hasEngine = true;
    print('Engine is installed.');
  }

  void addWheels() {
    hasWheels = true;
    print('Wheels are assembled.');
  }
}

void main() {
  var car = Car("NiceCar");
  car.assemble();
}
