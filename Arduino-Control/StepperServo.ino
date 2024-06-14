#include <Servo.h>
#include <TinyStepper_28BYJ_48.h>

/*#For Stepper
 * Angle /step 11.52 degree
 * 360 : 11.52 = 32 step
 * Gear ratio 64:1
 * 32 step * 64 ratio = 2048
*/
const int StepPerRev = 2048;

const int MOTOR_IN1_PIN = 8;
const int MOTOR_IN2_PIN = 9;
const int MOTOR_IN3_PIN = 10;
const int MOTOR_IN4_PIN = 11;

TinyStepper_28BYJ_48 stepper1;

String cmd = "Commands: \r";

/*#For Servo
  1. midpoint 1450
  2. maxpoint 2400
  3. minpoint 500
*/
Servo servo1;
int pos = 0; //Servo angle default

void calibrate_servo(){
  servo1.write(10);
  delay(1000);
  
  for(int i = 0; i <=3; i++){
    GRIP();
    Serial.println("Status: Grip");
    delay(1000);
    OPEN();
    Serial.println("Status: Open");
    delay(1000);
  }
  Serial.println("Finish calibrating servo");
}

void calibrate_stepper(){
  stepper1.setSpeedInStepsPerSecond(256);
  stepper1.setAccelerationInStepsPerSecondPerSecond(512);
  stepper1.moveRelativeInSteps(StepPerRev);
  delay(1000);
  for(int j = 1; j<=6; j++){
  stepper1.moveRelativeInSteps(341);
  Serial.println("60 degree turn");
  delay(1000);
  }
  Serial.println("Finish calibrating Stepper");
}

void GRIP(){
  for(pos = 10; pos <=43; pos +=1){
    servo1.write(pos);
    delay(7);
  }
}

void OPEN(){
  for(pos = 43; pos >=10; pos -=1){
    servo1.write(pos);
    delay(7);
  }
}


void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1000);
  stepper1.connectToPins(MOTOR_IN1_PIN, MOTOR_IN2_PIN, MOTOR_IN3_PIN, MOTOR_IN4_PIN);
  servo1.attach(6);
  servo1.write(10);

  stepper1.setSpeedInStepsPerSecond(256);
  stepper1.setAccelerationInStepsPerSecondPerSecond(1000);
}

void loop() {
  while(Serial.available() == 0){
    
  }
  cmd = Serial.readStringUntil('\r');

  if(cmd == "calibrate"){
    Serial.println("Starting calibration");
    calibrate_servo();
    calibrate_stepper();
    Serial.println("Finish Calibration");
  }

  if (cmd == "GRIP"){
    delay(10);
    GRIP();
    delay(100);
    Serial.println("FINISH GRIP");
  }
  if(cmd == "RTT"){
    stepper1.moveRelativeInSteps(112); //Real command
    Serial.println("FINISH ROTATE");
  }
  if(cmd == "FRTT"){
    stepper1.moveRelativeInSteps(341);
    Serial.println("FINISH ROTATE");
  }
  if(cmd == "UNGRIP"){
    delay(10);
    OPEN();
  }
}
