#include <XBee.h>

XBee xbee = XBee();

Rx16Response rx16 = Rx16Response();

void setup()
{
  Serial1.begin(9600);
  xbee.begin(Serial1);
  Serial.begin(9600);
}

void loop()
{
  xbee.readPacket(1000);
  if (xbee.getResponse().isAvailable())	{

    if (xbee.getResponse().getApiId() == RX_16_RESPONSE){
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
      /*for(int i=0;i < rx16.getDataLength(); i++){
        Serial.print(rx16.getData(i));
        Serial.print(" ");
      }
      //Serial.println("");
      */
    }

  } else if(xbee.getResponse().isError()){
      // error handling
      switch (xbee.getResponse().getErrorCode()){
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
