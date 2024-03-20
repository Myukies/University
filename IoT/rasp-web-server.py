from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on')
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return 'LED turned on'

@app.route('/off')
def turn_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return 'LED turned off'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
