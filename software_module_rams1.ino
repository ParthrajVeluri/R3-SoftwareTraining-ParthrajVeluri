/* Software Module by Parthraj Veluri */
/* Setup; Initialize all I/O pins with Input pins
	as pullup */
void setup()
{
	pinMode(1,OUTPUT);
    pinMode(2,OUTPUT);
    pinMode(3,OUTPUT);
  	pinMode(4,OUTPUT);
 	pinMode(8,INPUT_PULLUP);
  	pinMode(9,INPUT_PULLUP);
  	pinMode(7,INPUT_PULLUP);
  	pinMode(6,INPUT_PULLUP);
}

/* Function setting both motors to rotate counter clockwise */
void moveBackward(int x, int y){
  	digitalWrite(x,LOW);
    digitalWrite(y,HIGH);
  }

/* Function setting both motors to rotate clockwise */
void moveForward(int x, int y){
  	digitalWrite(x,HIGH);
    digitalWrite(y,LOW);
}

/* Function stopping both motors */
void stop(int x, int y){
	digitalWrite(x,LOW);
    digitalWrite(y,LOW);
}
  
void loop()
{
  /* Initializing variables */
  /* Motor F means motor will go forward if motor F is set HIGH */
  /* Motor B means motor will go backward if motor B is set HIGH */
  	int motor2_F = 1;
  	int motor2_B = 2;
  	int motor1_F = 4;
  	int motor1_B = 3;
  	int switch_1 = 8;
  	int switch_2 = 9;
  	int switch_3 = 7;
  	int switch_4 = 6; 
  
 
    
  if(digitalRead(switch_1)==LOW){
    /* Motors move forward */
  	moveForward(motor2_F,motor2_B);
    moveForward(motor1_F,motor1_B);
  }else if(digitalRead(switch_2)==LOW){
    /* Motors move backward */
  	moveBackward(motor1_F,motor1_B);
    moveBackward(motor2_F,motor2_B);
  }else if(digitalRead(switch_3)==LOW){
    /* Motors turn right */
    moveForward(motor1_F,motor1_B);
    moveBackward(motor2_F,motor2_B);
  }else if(digitalRead(switch_4)==LOW){
    /* Motors turn left */
    moveBackward(motor1_F,motor1_B);
    moveForward(motor2_F,motor2_B);
  }else{
    /* Motors do no move */
    stop(motor1_F,motor1_B);
    stop(motor2_F,motor2_B);
  }  
}

