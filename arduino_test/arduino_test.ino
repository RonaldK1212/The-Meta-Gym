long randNumber = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(A3));
}

void loop() {
  // put your main code here, to run repeatedly:
  long x = random(50);

  if(x%2 == 0){
    randNumber += x;
  }
  else randNumber -= x;
  Serial.print(millis());
  Serial.print(",");
  Serial.println(randNumber);
  delay(10);
  
}
