#!/bin/bash
# Displays the allowed HTML methods to be used on a URL
curl -sI "$1" | grep "Allow:" | cut -d" " -f2-
