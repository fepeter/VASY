#include <SoftwareSerial.h>
#include <Printers.h>
#include <XBee.h>



// Scetch to com with other Xbee
int TX = 18;
int RX = 19;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);

  Serial1.begin(9600);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int receive;
  
  
  if(Serial1.available()){
    receive = Serial1.read();
    Serial1.write(receive);
  }
  if(receive != 0){
    Serial.println(receive, DEC);
    analogWrite(LED_BUILTIN, receive);
  }


  
  
  
  
}
