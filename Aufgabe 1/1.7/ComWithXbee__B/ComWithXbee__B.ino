#include <XBee.h>

XBee xbee = XBee();

int packetnumber;
uint8_t payload[] = { 'I' };

Rx16Response rx16 = Rx16Response();
Tx16Request tx16 = Tx16Request(0x2, payload, sizeof(payload));

void setup()
{
  Serial1.begin(9600);
  xbee.begin(Serial1);
  Serial.begin(9600);
}

void loop()
{
  if (xbee.readPacket(1000) {
    if (xbee.getResponse().isAvailable())	{
        //There is a response
        if (xbee.getResponse().getApiId() == RX_16_RESPONSE) {
          //Its a Response packet with payload
          xbee.getResponse().getRx16Response(rx16);
          //print Sender Adress
          Serial.print("Sender: ");
          Serial.println(rx16.getRemoteAddress16());
          //print RSSI
          Serial.print("RSSI: ");
          Serial.println(rx16.getRssi());
  
          //print payload
          payload[0] = rx16.getData(0);
          Serial.print("Received Paket: ");
          Serial.print(payload[0]);
  
          //Send back the received packet number
          xbee.send(tx16);
          
          //TODO check tx status
        }
      } else if (xbee.getResponse().isError()) {
        // error handling
        switch (xbee.getResponse().getErrorCode()) {
          case CHECKSUM_FAILURE:
            Serial.println("CHECKSUM FAILURE");
            break;
          case PACKET_EXCEEDS_BYTE_ARRAY_LENGTH:
            Serial.println("PACKET_EXCEEDS_BYTE_ARRAY_LENGTH");
            break;
          case UNEXPECTED_START_BYTE:
            Serial.println("UNEXPECTED_START_BYTE");
            break;
          default:
            Serial.println("UNEXPECTED_ERROR");
            break;
        }
      }	else {
        Serial.println("No Response Available");
      }
  }
}
