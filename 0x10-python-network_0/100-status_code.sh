#!/bin/bash
# Displays the status code of a URL without using redirects or pipes
curl -so /dev/null -Iw "%{http_code}" "$1"
