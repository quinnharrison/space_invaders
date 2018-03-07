#define X_IN A2
#define Y_IN A1

#define ZzZz A0

void setup(){
  Serial.begin(9600);
  digitalWrite(ZzZz, LOW);
}
void loop(){
  int x,y;
  char c;
  //read pot voltages
  x = analogRead(X_IN);
  y = analogRead(Y_IN);
  
  x = map(x, 0, 1023, 0, 10) - 5;
  y = map(y, 0, 1023, 0, 10) - 5;

  // if somebody wants the data
  if(Serial.available()>0){
    //send the r,g,b values
    c = Serial.read();
    if (c == 'p'){
      Serial.print(x);
      Serial.print(',');
      Serial.println(y);
    } else if( c== 'd'){
      digitalWrite(ZzZz, HIGH);
      delay(1000);
      digitalWrite(ZzZz, LOW);
    
    }
    
    //finish the transimission with /n
  }
}
