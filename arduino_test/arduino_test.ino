long randNumber = 1000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  randomSeed(analogRead(A3));
  
}
float pi = 3.14;
void loop() {
  // put your main code here, to run repeatedly:
  float x = random(250);
  int y = (x+250)*sin(((millis()*2*pi)/2000))+700;
  y = map(y, 0, 820, 0, 4000);
  Serial.print(y);
  Serial.print(",");
  Serial.println(millis());
  delay(60);
  
}
