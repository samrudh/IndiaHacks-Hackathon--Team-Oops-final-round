#!/bin/bash
{
    python2.7 send.py
    sleep 1
    echo "sent: done"
}&
{
python2.7 delete.py
python2.7 ttttttt.py
sleep 1
echo "sent: done for second rpi"
}

