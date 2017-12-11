#include <XBee.h>

XBee xbee = XBee();
int packetnumber = 0;
uint8_t payload[] = { 'H' };
unsigned long sendrectime[2][1000];
int
// 0x40E4937A
//XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x40F301A5);

Tx16Request tx16 = Tx16Request(0x3, payload, sizeof(payload));

Rx16Response rx16 = Rx16Response();
Rx64Response rx64 = Rx64Response();

TxStatusResponse txStatus = TxStatusResponse();

uint8_t rssi = 0;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  Serial1.begin(9600);
  xbee.setSerial(Serial1);
}

void loop() {
  sendrectime[0][packetnumber] = millis();
  payload[0] = packetnumber;


  // Send Packet
  xbee.send(tx16);
  Serial.print("PacketNo: ");
  Serial.print(packetnumber);
  Serial.print(" Time: ");
  Serial.println(sendrectime[0][packetnumber]);
  packetnumber++;

  // wait for response packet
  if (xbee.readPacket(5000)) {
    // There is a packet
    if (xbee.getResponse().getApiId() == TX_STATUS_RESPONSE) {
      // Its a state packet
      xbee.getResponse().getTxStatusResponse(txStatus);

      // get the delivery status, the fifth byte
      if (txStatus.getStatus() == SUCCESS) {
        // success.  time to celebrate
        Serial.println("Sucess");
      }
      else {
        // the remote XBee did not receive our packet. is it powered on?
        Serial.println("Sending Failed");
      }
    }

    if (xbee.getResponse().getApiId() == RX_16_RESPONSE) {
      //Read packet (with payload)
      xbee.getResponse().getRx16Response(rx16);

      //print Sender Adress
      Serial.print("Sender: ");
      Serial.println(rx16.getRemoteAddress16());
      //print RSSI
      Serial.print("RSSI: ");
      Serial.println(rx16.getRssi());

      //print payload
      Serial.print("Received Paket: ");
      int paketnumber = rx16.getData(0);
      unsigned long t = rx16.getData(1);
      Serial.print(paketnumber);
      Serial.print(" ");
      Serial.println(t);


    }
  }
  else if (xbee.getResponse().isError()) {
    //nss.print("Error reading packet.  Error code: ");
    Serial.print("Error: ");
    Serial.println(xbee.getResponse().getErrorCode());
    // or flash error led
  }
  else {
    // local XBee did not provide a timely TX Status Response.  Radio is not configured properly or connected
    Serial.println("Some Bad shit");
  }
  delay(200);
}
