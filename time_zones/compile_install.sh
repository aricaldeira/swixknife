#!/bin/bash

sudo rm /usr/share/zoneinfo/SPM
sudo rm /usr/share/zoneinfo/NT4
sudo rm /usr/share/zoneinfo/NT6
sudo rm /usr/share/zoneinfo/Sezimal -rf
sudo rm /usr/share/zoneinfo/Dozenal -rf
sudo rm /usr/share/zoneinfo/Natural -rf

sudo zic spm_and_natural_time_zones.txt
