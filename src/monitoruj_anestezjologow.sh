#!/bin/bash

while true; do
    rm nazwiska.txt 
    for fn in `./pokaz_anestezjologow.sh`; do
	zgrep '<td colspan="2" class="tresc1k leftThinBtn"' "$fn" | head -3 | tail -1 | cut -d\  -f 14,15,16,17,18,19,20>> nazwiska.txt
    done
    cat nazwiska.txt
    cat nazwiska.txt | wc -l
    sleep 120
done


