double time_old, dt;
double integral, error_old = 0;
double kp, kd, ki;
double target_voltage = 5.0;

void setup()
{
  kp = 0.00005;
  ki = 50;
  kd = 0.00005;
  time_old = 0;
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  pinMode(A0,INPUT);
  analogWrite(3, 0);
  for(int i = 0; i < 50; i++)
  {
    Serial.print(target_voltage);
    Serial.print(",");
    Serial.println(0);
    delay(100);
  }
  delay(100);
}

void loop()
{
  double time_now = millis();
  dt = (time_now - time_old)/1000.00;
  time_old = time_now;

  double actual_voltage = analogRead(A0)*5.0/1023;
  double error_now = target_voltage - actual_voltage;
  
  integral += error_now*dt;
  double derivative = (error_now - error_old)/dt;
  error_old = error_now;
  double output_PWM = kp*error_now + ki*integral + kd*derivative;

  analogWrite(3, output_PWM);

  // Setpoint VS Actual
  Serial.print(target_voltage);
  Serial.print(",");
  Serial.println(actual_voltage);

  delay(300);
}
