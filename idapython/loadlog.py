#!/usr/bin/env pythong
#original author dereko (?) http://deroko.phearless.org/
import	idaapi
import  idc
import	struct
import  colorsys

def build_color_list():
        clist = [];
        
        r = 0x00/255.0;
        g = 0x00/255.0;
        b = 0xff/255.0;
        
        (h,s,v) = colorsys.rgb_to_hsv(r,g,b);
        s -= 0.30;
        for x in range(0,12):
                (r,g,b) = colorsys.hsv_to_rgb(h,s,v);
                #it's BGR
                ida_color = (int(b*255) << 16) + (int(g*255)<<8) + int(r*255);
                clist.append(ida_color); 
                s -= 0.05;
        clist.reverse();       
        return clist;

def main():
        clist = build_color_list();
        
	filepath = idaapi.askfile_c(False, "*.*", "Pin log file");
	imagebase = idaapi.get_imagebase();
	try:
		f = open(filepath, "rb");
	except:
		print("Need log file to parse data...");
		return;
	buff = f.read();
	for index in range(0, len(buff)):
		exec_count = ord(buff[index]);
		if exec_count == 0:
			continue;
		
		exec_count = exec_count / 10;
		if exec_count > 11: exec_count = 11;
		        
		ida_color = clist[exec_count];

		idc.SetColor(imagebase + index, CIC_ITEM, ida_color);

        
if __name__ == "__main__":   
	main();
