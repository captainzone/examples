# -*- coding:utf-8 -*-
import os
import argparse, sys
import signal 
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--sc', action='store_true')
parser.add_argument('--rs', action='store_true')
parser.add_argument('--ac', action='store_true')
parser.add_argument('--psc', action='store_true')
parser.add_argument('--ak', action='store_true')
parser.add_argument('--aps', action='store_true')
parser.add_argument('--synchc', action='store_true')
parser.add_argument('--syncch', action='store_true')

args = parser.parse_args()

if args.sc:
    os.system('docker run --runtime=nvidia -v data:/home/captainzone/ ufoym/deepo bash')
if args.rs:
    os.system('docker restart amazing_snyder')
if args.ac:
    cmd=['docker attach amazing_snyder']
    proc = subprocess.Popen(cmd)
    import time
    time.sleep(1000)
    os.kill(proc.pid,signal.SIGINT)
if args.psc:
    os.system('docker ps -a')
if args.aps:
    os.system('docker stop $(docker ps -a -q)')
if args.ak:
    os.system('docker rm $(docker ps -a -q)')
if args.synchc:
    os.system('docker cp ~/repo/examples amazing_snyder:/home/captainzone/repo/')
if args.syncch:
    os.system('docker cp amazing_snyder:/home/captainzone/repo/examples/. ~/repo/')
