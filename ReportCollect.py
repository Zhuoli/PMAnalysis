'''
Created on Mar 11, 2014

@author: CT61557
'''
import os
from os.path import join
import Image
from numpy import * 



for root,dirs,files in os.walk('../result'):    
    for dir in dirs:
        project = dir
        dir=root+'/'+dir
        kp=Image.open(dir +'/Knowledge Portal visitsRate.png')
        pr=Image.open(dir+'/Project Repository visitsRate.png')
        SIZE = kp.size
        new_size=(SIZE[0],SIZE[1]*2)
        new_im = Image.new("RGBA", new_size) 
        new_im.paste(kp, (0,0))
        new_im.paste(pr, (0,SIZE[1]))
        new_im.save(dir+'/report.jpg')
        new_im.save('../imgs/' + project+'_report.jpg')
        
