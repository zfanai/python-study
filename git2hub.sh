#!/bin/bash
echo 'git code to hub'
./gitadd.sh
./gitcommit.sh  "$1"
./gitpush.sh
echo 'finish.'
