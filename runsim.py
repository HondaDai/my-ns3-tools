#!/usr/bin/env ruby

import sys
import os
import re
import subprocess
import time


argc = len(sys.argv)

if argc == 1:
  print("You should pass 1+ arguments.")


filepath = sys.argv[1]
debug = False
if argc > 2:
  if sys.argv[2] == "debug":
    seeclass = [
      "MySim", 
      "BulkSendApplication",
      "UdpEchoClientApplication",
      "UdpEchoServerApplication",
      "OnOffApplication",
      "PacketSink",
    ]
    build_log = (lambda s:"%s=logic|prefix_func:DcfManager=error" % s)
    val = ":".join(map(build_log, seeclass ) )

    os.putenv("NS_LOG", val)
    debug = True
  else:
    os.putenv("NS_LOG", sys.argv[2])
else:
  content = open(filepath).read()
  m = re.search('NS_LOG_COMPONENT_DEFINE\s*[(]["](.+?)["][)]', content)
  if m:
    # print("%s=*" % (m.group(1)))
    os.putenv("NS_LOG", "%s=logic|prefix_func:DcfManager=error" % (m.group(1))) # level_all|prefix_func
  else:
    os.putenv("NS_LOG", "")

# directly modify build/c4che/_cache.py
# os.putenv("CFLAGS", "-Wno-error=unused-but-set-variable -Wno-tautological-compare") # make warning not be the error

# print("./waf --run %s" %(filename))
command = "./waf --run %s " %(filepath.split(".")[0])

# print(command)

def alert(msg):
  os.system("osascript -e 'tell app \"System Events\" to display dialog \"%s\"' >/dev/null 2>&1" % (msg) )


if debug:
  os.system("rm debug.log")
  os.system("echo '%s' > debug.log" % (time.strftime("%Y-%m-%d %H:%M:%S")) )
  os.system("%s >> debug.log 2>&1" % (command))
  alert("%s finished" % (filepath))
  os.system("subl debug.log")
  print("output to debug.log")
else:
  os.system(command)

