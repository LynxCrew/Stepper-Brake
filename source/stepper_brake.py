class StepperBrakeEnablePin:
    def __init__(self, enable, mcu_pin):
        self.enable = enable
        self.mcu_pin = mcu_pin
        self.mcu_enable = self.enable.mcu_enable
        self.enable.mcu_enable = self

    def set_digital(self, print_time, value):
        if not value:
            self.mcu_pin.set_digital(print_time, value)
        self.mcu_enable.set_digital(print_time, value)
        if value:
            self.mcu_pin.set_digital(print_time, value)


class StepperBrake:
    def __init__(self, config):
        self.config = config
        self.printer = config.get_printer()
        ppins = self.printer.lookup_object("pins")
        self.mcu_pin = ppins.setup_pin("digital_out", config.get("pin"))
        self.scale = 1.0
        self.stepper_names = config.getlist("stepper", None)
        self.stepper_enable = self.printer.load_object(config, "stepper_enable")
        self.printer.register_event_handler("klippy:ready", self._handle_ready)
        self.printer.register_event_handler("klippy:connect", self._handle_connect)

    def _handle_connect(self):
        all_steppers = self.stepper_enable.get_steppers()
        if self.stepper_names is None:
            self.stepper_names = all_steppers

    def _handle_ready(self):
        for stepper_name in self.stepper_names:
            StepperBrakeEnablePin(
                self.stepper_enable.lookup_enable(stepper_name).enable, self.mcu_pin
            )


def load_config_prefix(config):
    return StepperBrake(config)
