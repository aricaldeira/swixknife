#!/bin/bash

rm *.woff2

#
# Formato WOFF2
#
woff2_compress Andika-Bold.ttf
woff2_compress Andika-BoldItalic.ttf
woff2_compress Andika-Italic.ttf
woff2_compress Andika-Regular.ttf

woff2_compress GentiumPlus-Bold.ttf
woff2_compress GentiumPlus-BoldItalic.ttf
woff2_compress GentiumPlus-Italic.ttf
woff2_compress GentiumPlus-Regular.ttf
