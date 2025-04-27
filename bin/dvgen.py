#!/usr/bin/env python3

import argparse
import jinja2

def do_ut(name):
    print("UT generation start")


def main():
    parser = argparse.ArgumentParser(description="DVGen script")
    parser.add_argument('-ut', action='store_true', help='Enable UVM generation')
    parser.add_argument('-it', action='store_true', help='Enable UVM generation')
    parser.add_argument('-st', action='store_true', help='Enable UVM generation')
    
    parser.add_argument('-name', type=str, required=True, help='Specify the name')
    args = parser.parse_args()

    if args.ut: 
        do_ut(args.name)

if __name__ == "__main__":
    main()