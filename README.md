# LynxCrew Stepper-Brake Plugin

## What does it do:
This plugin enables a stepper_brake config section in Kalico/Klipper if you are
using either an Electromagnetic Stepper Brake or a pcb that shorts out the
phases of your steppers to increase the detent torque.
If configured, it will enable a defined output pin immediately after drivers are turned on
(to disengage the brake) and disable it immediately before drivers are turned
off (to engage the break)
order of operations still has to be discussed!

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
!!This does only work if your drivers have an enable pin as it hooks directly
into the enable pin code!!
(on the other hand, drivers without an enable pin are always active and thus
should not need a brake, if you feel like you still need it, open an issue and
I will try to implement it)
just add
```
[stepper_brake my_stepper_brake]
pin: 
#   the pin to be switched when steppers turn on or off
stepper:
#   the steppers that should cause the pin to switch.
#   If this parameter is not specified, the module will listen to all steppers
disengage_before_enable: False
#   By default the brake will be disengaged after the drivers are turned on and
#   engaged before they are turned off.
#   Set this to true if that causes tmc errors for you to switch the order of
#   operations.
