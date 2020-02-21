#!/bin/bash

dateout=$(date +"%s")

for i in {1..100}
do
	curl -s 172.31.39.66:5000/api/valinc
	echo
done > ~/againstapp1api/testagainstapp1-$dateout.log
