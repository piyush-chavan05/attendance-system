#include <SPI.h>
#include <MFRC522.h>

#define RESET_PIN 9
#define SELECT_PIN 10

MFRC522 rfidReader(SELECT_PIN, RESET_PIN);

void setup() {
  Serial.begin(9600);
  SPI.begin();
  rfidReader.PCD_Init();
}

void loop() {
  if (!rfidReader.PICC_IsNewCardPresent() || !rfidReader.PICC_ReadCardSerial()) {
    return;
  }

  String cardNumber = "";
  for (byte i = 0; i < rfidReader.uid.size; i++) {
    cardNumber += String(rfidReader.uid.uidByte[i], HEX);
  }

  Serial.println(cardNumber);

  rfidReader.PICC_HaltA();
  rfidReader.PCD_StopCrypto1();
  delay(1000);
}