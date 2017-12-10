// Scetch to com with other Xbee
int TX = 18;
int RX = 19;

bool openfire;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);

  Serial1.begin(9600);
  Serial.begin(9600);

  
  
}

void loop() {
  byte fire;
  byte receive;
   
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    fire = Serial.read();
    if(fire == 'f'){
      openfire = true;
    }
    if(fire == 's'){
      openfire = false;
    }
  }

  if(openfire){
    Serial1.println(1);
    Serial.println("Fireing");
  } else {
    Serial1.println(0);
    Serial.println("silence");
  }
  
  if(false){
     digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
     Serial.println("huhuh");
     Serial1.println("huhuh");
     delay(1000);                       // wait for a second
     digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
     delay(100);                 
  }
  delay(1000);
}
