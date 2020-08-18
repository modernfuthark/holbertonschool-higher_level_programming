#!/bin/bash
# Sends a POST request with the data email and subject
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
