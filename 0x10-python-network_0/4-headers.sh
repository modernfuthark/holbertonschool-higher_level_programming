#!/bin/bash
# Sends a GET request to a URL with the header variable HolbertonSchool-User-Id equalling 98
curl -s "$1" -X GET -H "HolbertonSchool-User-Id: 98"
