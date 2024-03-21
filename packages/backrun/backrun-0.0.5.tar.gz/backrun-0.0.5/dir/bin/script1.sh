#!/bin/bash

log(){
    echo `date "+%Y-%m-%d %H:%M:%S"` $*
}

log started as user `whoami`
sleep 10
>&2 log "error"
log finished

