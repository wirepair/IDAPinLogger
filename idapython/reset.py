#!/usr/bin/env pythong
# modified by @_wirepair to 'white out' or diff two IDAPinLogger runs.
import idaapi
import idc
import struct
import colorsys

def main():
	ida_color = 0xFFFFFFFF
	start = FirstSeg()
	end = SegEnd(start)
	while(start != idc.BADADDR):
                
                for i in range(start, end):
                        idc.SetColor(i, CIC_ITEM, ida_color);
                start = NextSeg(start)
                end = SegEnd(start)
                

        
if __name__ == "__main__":   
	main()
