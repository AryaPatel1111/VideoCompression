# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 11:05:09 2020

@author: aryam
"""

import os

os.system('cmd /c "ffmpeg -i 2.mp4 -vcodec libx265 -crf 28 output.mp4"')
