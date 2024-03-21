#!/bin/bash

log(){
    echo `date "+%Y-%m-%d %H:%M:%S"` $*
}

log started
sleep 10
>&2 log "error"
log finished

