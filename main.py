from microdot import Microdot, send_file
from machine import Pin

# Mapping of board pins to GPIO
pin_map = {0: 16, # I/O
           1: 5,  # I/O, SCL
           2: 4,  # I/O, SDA
           3: 0,  # I/O, 10k pull-up
           4: 2,  # I/O, 10k pull-up?
           5: 14, # I/O, SCK, BUILTIN_LED
           6: 12, # I/O, MISO
           7: 13, # I/O, MOSI
           8: 15, # I/O, 10k pull-down, SS
           }

pins = {}

app = Microdot()

@app.route('/')
async def index(request):
    return send_file('index.html')

@app.route('/pins/get/<int:pin_number>')
async def get_pin(request, pin_number):
    
    # Check if the pin number is valid
    if pin_number < 0 or pin_number > 8:
        return 'Invalid pin number', 400

    # Initialize the pin if required
    if pin_number not in pins:
        pins[pin_number] = Pin(pin_map[pin_number], Pin.OUT, value=1)

    # Get the current state of the pin
    state = int(pins[pin_number].value() == 0)
    return f"{state}"

@app.route('/pins/set/<int:pin_number>/<int:value>')
async def get_pin(request, pin_number, value):
    
    # Check if the pin number is valid
    if pin_number < 0 or pin_number > 8:
        return 'Invalid pin number', 400
    
    # Check if the pin value is valid
    if value < 0 or value > 18:
        return 'Invalid pin value', 400

    # Initialize the pin if required
    if pin_number not in pins:
        pins[pin_number] = Pin(pin_map[pin_number], Pin.OUT, value=1)

    # Set the current state of the pin
    pins[pin_number].value(value == 0)
    state = int(pins[pin_number].value() == 0)
    return f"{state}"

app.run(port=80)
#app.run(port=80, debug=True)
