#!/bin/bash

#this instruction is to be run on pi for flashing into vaman

sudo python3 /home/shreyash/armencoder/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --port /dev/ttyACM0  --appfpga top.bin --m4app blink.bin --mode m4-fpga --reset
