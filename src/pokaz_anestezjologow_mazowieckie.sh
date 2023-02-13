#!/bin/bash

zgrep -rl "Lekarska w Warszawie" results | xargs zgrep -l nestez

# | xargs zgrep -rl "20-\d\d\d"
