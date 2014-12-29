Boilerplate code is annoying and sometimes there can be a lot of it working with [Raspberry Pi GPIO](https://pypi.python.org/pypi/RPi.GPIO). I got tired of setting the board mode and declaring GPIO channels in every script so I made a library that uses a config file instead. In addition to getting rid of the boilerplate, **Pi-Pin-Manager** has the added benefit of pulling the configuration out of the code. This means you can modify any pin's behavior without ever touching a Python file or having to redeploy your program.


### Install It

```
pip install Pi-Pin-Manager
```

### Configure It

A config file, written in [YAML](http://en.wikipedia.org/wiki/YAML), is used to define the initial pin setup. If a pin is not defined here it will not be available to the `PinManager`. The following snippet shows an example configuration file:

```yaml
18:
  mode: OUT
  initial: HIGH
23:
  mode: OUT
  initial: LOW
24:
  mode: IN
  event: RISING
  handler: do_something
  bounce: 200
```

* Add a numbered element for each pin to enable
* `mode` - This controls whether the pin will be used for input or output. Accepted values are: `IN`, `OUT`. (Required)
* `initial` - This controls the starting value of the pin. Accepted values are: `LOW`, `HIGH`. (Optional - defaults to `LOW`)
* `resistor` - This controls the software defined pull up/pull down resistor available in the Broadcom SOC. Accepted values are: `PUD_UP`, `PUD_DOWN`. (Optional - defaults to none)
* `event` - This is used in combination with a pin set to input mode (`mode: IN`). Accepted values are: `RISING`, `FALLING`, `BOTH`.
* `handler` - This is used in combination with an `event` to designate a function to call when an `event` happens. This value should correspond to a function defined in your handler class.
* `bounce` - This can be used when an `event` is defined to prevent multiple `handler` calls being fired accidentally. The value is the number of milliseconds to wait before detecting another `event`.

**Note:**

For full documentation about available GPIO input pin configurations see the [documentation](http://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/).


### Use It (No Events)

```python
from pi_pin_manager import PinManager


pins = PinManager(config_file='path/to/config/file.yml')


# Read a pin
result = pins.read(18)

# Write to a pin
pins.write(19, 1)

# Turn pin on
pins.on(19)

# Turn pin off
pins.off(19)

# Get configuration for a pin
result = pins.get_config(23)
```

### Use It (With Events)

If an `event` and `handler` have been defined for a pin in the config file, then you must also provide a class that contains the callbacks to execute. Each method you add to this class should match the name of a `handler` value. Based on the example code below, `handler: do_something` is expected in the config file `path/to/config/file.yml`.

```python
from pi_pin_manager import PinManager


class EventHandlers(object):

    def do_something(self, pin_number):
        # Whatever you want to trigger when an event is detected goes here
        print('pin {0}'.format(pin_number))


pins = PinManager(config_file='path/to/config/file.yml', event_handlers=EventHandlers())
```

**Exceptions:**

This package may raise the following custom exceptions:

* `PinNotDefinedError` - This is raised when attempting to `read` or `write` to a pin that is not defined in the configuration file.
* `PinConfigurationError` - This is raised when attempting to perform an action on a pin that does not match its configuration. For example, trying to `write` to a pin not defined as `mode: OUT`.