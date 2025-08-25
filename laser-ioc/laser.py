import socket
import RPi.GPIO as GPIO

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 1000)  # 1kHz frequency
pwm.start(0)

# Socket setup - listen on all interfaces
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('172.30.85.220', 5555)) 
sock.listen(1)

print("PWM Server listening on port 5555 (all interfaces)")

try:
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024).decode('utf-8').strip()
        
        if data.startswith("PWM_ENABLE"):
            enable = int(data.split()[1])
            if enable:
                pwm.start(0)
            else:
                pwm.stop()
                
        elif data.startswith("PWM_SET"):
            duty_cycle = float(data.split()[1])
            pwm.ChangeDutyCycle(duty_cycle)
        
        conn.close()
        
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    sock.close()
