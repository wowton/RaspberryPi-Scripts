#!/bin/bash

#author: WangTeng
#date  : 2017-05-05

read old_ip < ~/my_ip.txt
new_ip=$(curl ipinfo.io/ip)

sendMail(){
	#$1:subject
	#$2:content
	#$3:address
	echo "$2" | mutt -s "$1" $3
}

if [[ $old_ip != $new_ip ]];
then
	sendMail "IP is changed" $new_ip "brvton@gmail.com"
	echo $new_ip > ~/my_ip.txt
fi


