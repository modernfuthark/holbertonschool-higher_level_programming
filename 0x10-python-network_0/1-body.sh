#!/bin/bash
# Sends a GET request to a URL, if the response is of status code 200, display the content of the body.
if [ "$(curl -sLI "$1" -X GET | grep '200 OK' | cut -d' ' -f2)" -eq '200' ]; then
	curl -sL "$1";
fi
