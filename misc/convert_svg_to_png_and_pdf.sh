#!/bin/bash
inkscape --export-type png  *.svg
inkscape --export-type pdf --export-text-to-path *.svg
