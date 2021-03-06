INPUT_MODE = 'IN'
OUTPUT_MODE = 'OUT'

HIGH = 'HIGH'
LOW = 'LOW'

PULL_UP_RESISTOR = 'PUD_UP'
PULL_DOWN_RESISTOR = 'PUD_DOWN'
NO_RESISTOR = 'PUD_OFF'

PIN_MODES = (INPUT_MODE, OUTPUT_MODE, )
PIN_INITIALS = (LOW, HIGH, )
PIN_RESISTORS = (PULL_UP_RESISTOR, PULL_DOWN_RESISTOR, NO_RESISTOR, )

PIN_RISING_EVENT = 'RISING'
PIN_FALLING_EVENT = 'FALLING'
PIN_BOTH_EVENT = 'BOTH'
PIN_EVENT_TYPES = (PIN_RISING_EVENT, PIN_FALLING_EVENT, PIN_BOTH_EVENT, )
