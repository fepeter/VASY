#include <SoftwareSerial.h>
#include <Printers.h>
#include <XBee.h>
// Scetch to com with other Xbee
int TX = 18;
int RX = 19;

int value = 1;
int dir = 1;
int delayTime = -1;
int calcTime = 1;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);

  //Serial1.begin(9600);
  Serial.begin(9600);
  Serial1.begin(9600);
}

void loop() {
  byte receive;

  
/*
  if(dir == 1){
    value++;
  } else {
    value--;
  }
  if(value > 255){
    dir = 0;
  } 
  if(value < 2){
    dir = 1;
  }
*/
  Serial.println(value);
  if(value == 1){
    value =255;
  } else {
    value = 1;
  }

  if(calcTime == 1){
    int time1 = millis();
    Serial1.write(value);
    while(!Serial1.available()){
      ;
    }
    
    receive = Serial1.read();
    if(receive != 0 && receive == value){
      int time2 = millis();
      delayTime = time2-time1;
      calcTime = 0;
      Serial.print("Measuring ");
      Serial.println(delayTime);
    }
    
    
   } else {
      Serial1.write(value);
      delay(delayTime);
      analogWrite(LED_BUILTIN, value);
      //Serial.print("Waited " );
      //Serial.println(delayTime);
      calcTime = 0;
   } 
  delay(200);
  Serial1.flush();
  
}

