#define X_IN A2
#define Y_IN A1

#define butt 7

void setup(){
  Serial.begin(9600);
  pinMode(butt, INPUT);
}
void loop(){
  int x,y,button;
  char c;
  //read pot voltages
  x = analogRead(X_IN);
  y = analogRead(Y_IN);
  button = digitalRead(butt);
  
  x = map(x, 0, 1023, 0, 10) - 5;
  y = map(y, 0, 1023, 0, 10) - 5;

  // if somebody wants the data
  if(Serial.available()>0){
    //send the r,g,b values
    c = Serial.read();
    if (c == 'p'){
      Serial.print(x);
      Serial.print(',');
      Serial.print(y);
      Serial.print(',');
      Serial.println(button);
    }
    
    //finish the transimission with /n
  }
}
