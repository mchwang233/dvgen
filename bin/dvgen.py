#!/usr/bin/env python3

import argparse
import jinja2

def main():
    parser = argparse.ArgumentParser(description="DVGen script")
    parser.add_argument('-uvm', action='store_true', help='Enable UVM generation')
    parser.add_argument('-name', type=str, required=True, help='Specify the name')
    args = parser.parse_args()

    if args.uvm:
        print("UVM generation enabled")
        print(args.name)

if __name__ == "__main__":
    main()