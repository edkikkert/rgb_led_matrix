RGB LED Banner
==============

##Intro
This is an [OpenCommunityCamp.org](http://opencommunitycamp.org/site/) project.
It features a 26 by 6 LED banner, remotely controlable by a webserver.

##Hardware
* ADDME

##Software
The parser.py parses the font file and sends text over serial to the Arduino
board. Arduino runs OCC2012\_LED.ino using the LED driver library of:
  https://github.com/adafruit/HL1606-LED-Strip

## Credits
 * Software wrapper Arduino       - Rick van der Zwet <info@rickvanderzwet.nl>
 * Python control client/server   - Karlo Luiten <mail@karloluiten.nl>
 * Hardware design/implementation - Ed Kikkert <ed@kikkert-online.nl>


##Special Thanks
To our sponsors:
 * [Optiver](http://www.optiver.com)
 * [Ziggo](http://www.ziggo.nl)


##Video Examples
* [Video](http://www.youtube.com/watch?v=K2JLcTTljiA)

##License
Unless otherwhere noted this code is licensed 2-clause BSD

===
Copyright (c) 2012, OpenCommunityCamp.org
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met: 

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer. 
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies, 
either expressed or implied, of the OpenCommunityCamp Project.
