#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX

const int led1 = 3;
const int led2 = 4;
const int led3 = 5;
const int led4 = 6;

String inStr;

class Device
{
 public:
  virtual void turnOn() = 0;
  virtual void turnOff() = 0;
};

class Led : public Device
{
  int pin;
 public:
  Led(int p)
  {
    pin = p;
    pinMode(pin, OUTPUT);
  }
  void turnOn()
  {
    digitalWrite(pin, HIGH);
  }
  void turnOff()
  {
    digitalWrite(pin, LOW);
  }
};

Led ledOne = Led(led1);
Led ledTwo = Led(led2);
Led ledThree = Led(led3);
Led ledFour = Led(led4);

void setup() {
  Serial.begin(9600);
  mySerial.begin(9600);
}

void loop() {
  while (mySerial.available() > 0) {
    char inChar = (char)mySerial.read();
    inStr += inChar;
    if (inStr.endsWith("#")) {
      if (!strcmp(inStr.c_str(), "*turn on light one#")) {
        ledOne.turnOn();
      }
      if (!strcmp(inStr.c_str(), "*turn off light one#")) {
        ledOne.turnOff();
      }
      if (!strcmp(inStr.c_str(), "*turn on light two#")) {
        ledTwo.turnOn();
      }
      if (!strcmp(inStr.c_str(), "*turn off light two#")) {
        ledTwo.turnOff();
      }
      if(!strcmp(inStr.c_str(), "*turn on light three#")) {
        ledThree.turnOn();
      }
      if (!strcmp(inStr.c_str(), "*turn off light three#")) {
        ledThree.turnOff();
      }
      if(!strcmp(inStr.c_str(), "*turn off light four#")) {
        ledFour.turnOn();
      }
      if (!strcmp(inStr.c_str(), "*turn off light four#")) {
        ledFour.turnOff();
      }
      if(!strcmp(inStr.c_str(), "*turn on all lights#")) {
        ledOne.turnOn();
        ledTwo.turnOn();
        ledThree.turnOn();
        ledFour.turnOn();
      }
      if(!strcmp(inStr.c_str(), "*turn off all lights#")) {
        ledOne.turnOff();
        ledTwo.turnOff();
        ledThree.turnOff();
        ledFour.turnOff();
      }
      
      inStr = "";
    }
  }
}

