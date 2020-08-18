#!/bin/bash
# Runs cURL to get the body size of a url
curl -sI "$1" | grep "Content-Length" | cut -d" " -f2
