#!/usr/bin/env python
import sys
import shutil
import argparse
import os
parser = argparse.ArgumentParser(description='Copy Image Assets from Material Design to your Android Project, preview all here: https://google.github.io/material-design-icons/, place and run this script inside the material-icons-master folder')
parser.add_argument('group', type=str, help='The group eg. social, av, navigation')
parser.add_argument('name', type=str, help='The name of the icon eg. 3d_rotation, attach_file, poll')
parser.add_argument('color', type=str, help='color of the icon',choices=['black','white'])
parser.add_argument('dest', type=str, help='Desination res folder')
args = parser.parse_args()
dirs = map(lambda x: args.group+'/drawable-'+x+'/', ['hdpi', 'mdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi'])

for i in dirs:
    src = i+'_'.join(['ic', args.name.lower(), args.color.lower(), '48dp.png'])
    out_dir = args.dest+'/'+src.split('/')[1]
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print ("Creating", out_dir)
    dest = out_dir +'/'+src.split('/')[-1]
    
    print ("Copying", src, "to", dest)
    shutil.copy(src, dest)

