# LynxCrew Stepper-Brake Plugin

## What does it do:
This plugin enables a stepper_brake config section in Kalico/Klipper if you are
using either an Electromagnetic Stepper Brake or a pcb that shorts out the
phases of your steppers to increase the detent torque.

## Install:
SSH into you pi and run:
```
cd ~
wget -O - https://raw.githubusercontent.com/LynxCrew/Stepper-Brake/main/install.sh | bash
```

then add this to your moonraker.conf:
```
[update_manager stepper-brake]
type: git_repo
channel: dev
path: ~/stepper-brake
origin: https://github.com/LynxCrew/Stepper-Brake.git
managed_services: klipper
primary_branch: main
install_script: install.sh
```

## How to use:
just add
```
[stepper_brake my_stepper_brake]
pin: 
#   the pin to be switched when steppers turn on or off
stepper:
#   the steppers that should cause the pin to switch.
#   If this parameter is not specified, the module will listen to all steppers
