#include <XBee.h>

XBee xbee = XBee();
int paketnumber = 1;
uint8_t payload[] = { 'H', 'i' };
// 0x40E4937A
XBeeAddress64 addr64 = XBeeAddress64(0x0013a200, 0x40F301A5);

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
	unsigned long t = millis();
	payload[0] = paketnumber;
	payload[1] = t;

	// Send Paket
	xbee.send(tx16);
	Serial.print("PaketNo: ");
	Serial.print(paketnumber);
	Serial.print(" Time: ");
	Serial.println(t);
	paketnumber++;

	// wait for response paket
	if (xbee.readPacket(5000)) {
		// should be a znet tx status            	
		if (xbee.getResponse().getApiId() == TX_STATUS_RESPONSE) {
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
