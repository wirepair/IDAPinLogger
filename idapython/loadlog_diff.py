#!/usr/bin/env pythong
# original author dereko (?) http://deroko.phearless.org/
# modified by @_wirepair to 'white out' or diff two IDAPinLogger runs.
import	idaapi
import  idc
import	struct
import  colorsys

def main():
	filepath = idaapi.askfile_c(False, "*.*", "Pin log file");
	imagebase = idaapi.get_imagebase();
	try:
		f = open(filepath, "rb");
	except:
		print("Need log file to parse data...");
		return;
	buff = f.read();
	ida_color = 0xFFFFFFFF;
	for index in range(0, len(buff)):
		exec_count = ord(buff[index]);
		if exec_count == 0:
			continue;
		
		exec_count = exec_count / 10;
		if exec_count > 11: exec_count = 11;

		idc.SetColor(imagebase + index, CIC_ITEM, ida_color);

        
if __name__ == "__main__":   
	main();
