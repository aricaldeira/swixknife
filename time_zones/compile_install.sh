#!/bin/bash

sudo rm /usr/share/zoneinfo/GPM -rf
sudo rm /usr/share/zoneinfo/SPM -rf
sudo rm /usr/share/zoneinfo/NT4 -rf
sudo rm /usr/share/zoneinfo/NT6 -rf
sudo rm /usr/share/zoneinfo/Sezimal -rf
sudo rm /usr/share/zoneinfo/Dozenal -rf
sudo rm /usr/share/zoneinfo/Natural -rf

sudo zic gpm_time_zones.txt
sudo zic spm_time_zones.txt
sudo zic sezimal_time_zones.txt
sudo zic dozenal_time_zones.txt
