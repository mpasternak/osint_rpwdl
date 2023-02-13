#!/bin/bash

zgrep -rl Lubelska results | xargs zgrep -l anest 
