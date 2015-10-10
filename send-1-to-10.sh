#!/bin/bash
#ssh tutorial1@10.0.0.1 ITGSend -a 10.0.0.10 CSa -L 10.123.123.1 -X 10.123.123.1
ITGDec /tmp/ITGRecv*.log -v
#ITGDec /tmp/ITGRecv.log /tmp/combined.dat -c 1 /tmp/combined_stats.dat
#ITGDec /tmp/ITGRecv.log -l /tmp/ITGRecv.txt -o /tmp/octave.dat