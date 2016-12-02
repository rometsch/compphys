#!/bin/bash

mkdir video

ffmpeg -framerate 2 -i 4.5_5.5_n%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p video/4.5_5.5.mp4

ffmpeg -framerate 2 -i 0.0_10.0_n%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p video/0_10.mp4

ffmpeg -framerate 2 -i 0.0_30.0_n%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p video/0_30.mp4
