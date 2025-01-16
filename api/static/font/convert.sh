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

woff2_compress NotoSans-Regular.ttf
woff2_compress NotoSansMath-Regular.ttf
woff2_compress NotoSansSymbols-Regular.ttf
woff2_compress NotoSansSymbols2-Regular.ttf

woff2_compress DSEG14Classic-Regular.ttf

woff2_compress KsConstellationSymbolsFV.ttf
woff2_compress KsConstellationSymbolsCV.ttf
