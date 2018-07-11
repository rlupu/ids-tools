# Copyright (c) 2018 UPB
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Author: Irina Nicolae <irina_nicolae@outlook.com>, <rlupu@elcom.pub.ro>
#
from Tkinter import *
import threading, time
import nmap
import random
#import sys
#sys.setrecursionlimit(100000)

# clear fields at the end

class BotnetSynthesizer:
  def __init__(self, root):
    #self.spoof_adr_list = ['1.1.1.1','2.2.2.2','3.3.3.3']
    self.spoof_adr_list = []
'14.14.14.14','15.15.15.15','16.16.16.16','17.17.17.17','18.18.18.18','19.19.19.19','20.20.20.20','21.21.21.21','22.22.22.22','23.23.23.23','24.24.24.24','25.25.25.25','26.26.26.26',
'27.27.27.27','28.28.28.28','29.29.29.29','30.30.30.30']
    # main
    self.window = Toplevel(root)
    self.window.title("Botnet Traffic Synthesizer")
    self.window.configure(background="light blue")  # lightsteelblue
    self.window.geometry("1000x500+200+200")

    self.sVar = IntVar(self.window)
    self.rVar = IntVar(self.window)
    self.start_scan = BooleanVar(self.window)
    # photo
    self.photo = PhotoImage(file="bot.gif")
    Label(self.window, image=self.photo).grid(row=0, column=5, sticky=W)
    # label
    Label(self.window, text="Target", bg="light blue", fg="white", font="none 10 bold").grid(row=0, column=0,
                                                                                                 sticky=W)
    Label(self.window, text="Number of bots ", bg="light blue", fg="white", font="none 10 bold").grid(row=1, column=0,
                                                                                                 sticky=W)
    Label(self.window, text="Type of traffic", bg="light blue", fg="white", font="none 10 bold").grid(row=3, column=0,
                                                                                                 sticky=W)
    Label(self.window, text="Spoof", bg="light blue", fg="white", font="none 10 bold").grid(row=5, column=0, sticky=W)
    Label(self.window, text="Randomize", bg="light blue", fg="white", font="none 10 bold").grid(row=5, column=3, sticky=E)
    Label(self.window, text="Spoof addreses:", bg="light blue", fg="white", font="none 10 bold").grid(row=7, column=0,
                                                                                                 sticky=W)
    Label(self.window, text="Ports interval:", bg="light blue", fg="white", font="none 10 bold").grid(row=11, column=0,
                                                                                                 sticky=W)
    Label(self.window, text="start", bg="light blue", fg="white", font="none 10 bold").grid(row=11, column=2, sticky=W)
    Label(self.window, text="end", bg="light blue", fg="white", font="none 10 bold").grid(row=11, column=5, sticky=W)
    Label(self.window, text="overlap", bg="light blue", fg="white", font="none 10 bold").grid(row=11, column=16, sticky=E)
    Label(self.window, text="Rate", bg="light blue", fg="white", font="none 10 bold").grid(row=13, column=0, sticky=W)
    Label(self.window, text="Scan interval", bg="light blue", fg="white", font="none 10 bold").grid(row=14, column=0, sticky=W)
    # text entry
    self.target_adr = Entry(self.window, width=20,bg="white")
    self.target_adr.grid(row=0,column=1,sticky=W)
    self.bots = Entry(self.window, width=20, bg="white")
    self.bots.grid(row=1, column=1, sticky=W)
    self.traffic_type = Entry(self.window, width=20, bg="white")
    self.traffic_type.grid(row=3, column=1, sticky=W)
    self.start = Entry(self.window, width=20, bg="white")
    self.start.grid(row=11, column=1, sticky=W)
    self.end = Entry(self.window, width=20, bg="white")
    self.end.grid(row=11, column=4, sticky=W)
    self.overlapUI = Entry(self.window, width=20, bg="white")
    self.overlapUI.grid(row=11, column=15, sticky=E)
    self.spoof_adr = Entry(self.window, width=20, bg="white")
    self.spoof_adr.grid(row=7, column=1, sticky=W)
    self.min_rate = Entry(self.window, width=20, bg="white")
    self.min_rate.grid(row=13, column=1, sticky=W)
    self.scan_interval = Entry(self.window, width=20, bg="white")
    self.scan_interval.grid(row=14, column=1, sticky=W)
    # buttons
    Button(self.window, text="Add", width=5, command=self.addSource).grid(row=9, column=1, sticky=W)
    Button(self.window, text="Generate", width=8, command=self.setup).grid(row=26, column=3, sticky=SE)
    Button(self.window, text="Clear", width= 6, command=self.delete).grid(row=28,column=1, sticky=W)
    #self.operation = StringVar(self.self.window)
    #self.operation.set("generate")
    #self.operation_rbutton = Radiobutton(self.window, width=8, text="Generate", variable=self.operation, value="generate", indicatoron=0)
    #self.operation_rbutton.grid(row=26, column=3, sticky=SE)
    #self.operation_rbutton = Radiobutton(self.window, width=6, text="Stop", variable=self.operation, value="stop", indicatoron=0)
    #self.operation_rbutton.grid(row=28, column=1, sticky=W)
    # do self.operation.get() == 'stop'
    ##Radiobutton(self.window, width=8, text="Generate", command=self.setup, variable=self.start_scan, value=True, indicatoron=0).grid(row=26, column=3, sticky=SE)
    #will be used for stop and delete purposes
    ##Radiobutton(self.window, width=6, text="Clear", command=self.delete, variable=self.start_scan, value=False, indicatoron=0).grid(row=28, column=1, sticky=W)
    # do self.start_scan.get() == True


    # checkbuttons
    C1 = Checkbutton(self.window, state=ACTIVE, variable=self.sVar, onvalue=1, offvalue=0).grid(row=5, column=1)
    C2 = Checkbutton(self.window, state=ACTIVE, variable=self.rVar, onvalue=1, offvalue=0).grid(row=5, column=4)
    #Option Menu
    self.menu = StringVar(self.window)
    self.menu.set("Option")
    self.menu_option = OptionMenu(self.window, self.menu, "Continuity", "Gap")
    self.menu_option.grid(row=11, column=20, sticky=E)

    self.window.protocol("WM_DELETE_self.window", self.window.destroy)

  def addSource(self):
    source = self.spoof_adr.get()
    self.spoof_adr_list.append(source)
    self.spoof_adr.delete(0, 'end')  # delete(0, END)

  def delete(self):
    self.traffic_type.delete(0, 'end')
    self.target_adr.delete(0, 'end')
    self.bots.delete(0, 'end')
    self.start.delete(0, 'end')
    self.end.delete(0, 'end')
    self.overlapUI.delete(0, 'end')
    self.min_rate.delete(0, 'end')
    self.scan_interval.delete(0, 'end')
    self.start_scan = False


  def setup(self):
    traffic = self.traffic_type.get()
    target = self.target_adr.get()
    spoof = self.sVar.get()
    randomize = self.rVar.get()
    nb_bots = self.bots.get()
    ports_start = int(self.start.get())
    ports_end = int(self.end.get())
    overlap_percent = int(self.overlapUI.get())
    menu_option = self.menu.get()
    rate = self.min_rate.get()
    scan_interval = self.scan_interval.get()
    ports = []
    for i in range(ports_start, ports_end+1):
      ports.append(i)
    if menu_option == "Gap":
      gap = random.randint(2, len(ports))
      for i in range(gap):
        element = random.choice(ports)
        ports.remove(element)
    overlap = round(overlap_percent * len(ports) / 100)
    intervals = self.divide(ports, nb_bots,overlap)

    #if self.start_scan == True:
    self.generateTraffic(target, traffic, spoof, self.spoof_adr_list, randomize, intervals, nb_bots, rate, scan_interval)
    #else:
    #self.delete()


  def divide(self, ports, bots, overlap):
      intervals = {}
      k = 0
      j = 0
      numarator = len(ports)
      numitor = int(bots)
      while numitor != 0:
        list = []
        max_limit = int(round(numarator / numitor)) + overlap
        if numitor == 1: #one bot left
          lung_interval = numarator
        else:
          lung_interval = random.randint(2, max_limit)
          print numarator
        for i in range(int(k), int(k + lung_interval)):
          list.append(ports[i])
        k += lung_interval - overlap
        intervals[j] = list
        j += 1
        numitor -= 1
        numarator -= len(list)
      print(intervals)
      return intervals


  def nmapUDP(self,target, interval, spoof, source, randomize):
      # -r DONT RANDOMIZE
      time.sleep(random.randint(2, 10))
      scan_object = nmap.PortScanner()
      if spoof:
        if randomize:
          parameters = '-sU -e eth0 -S ' + str(source) + ' -T5'
        # scan_object.scan(target,interval, arguments = '-sU -e eth0 -S 141.85.161.236 -T5')
        else:
          parameters = '-sU -r -e eth0 -S ' + str(source) + ' -T5'
          # scan_object.scan(target,interval, arguments = '-sU -r -e eth0 -S 141.85.161.236 -T5')
      else:
        if randomize:
          parameters = '-sU -e eth0 -T5'
        # scan_object.scan(target,interval, arguments = '-sU -e eth0 -T5')
        else:
          parameters = '-sU -r -e eth0 -T5'
          # scan_object.scan(target,interval, arguments = '-sU -r -e eth0 -T5')
      scan_object.scan(target, interval, arguments=parameters)
      #scan_object.stop() stop thread

      # print scan_object.command_line()
     # state = scan_object[target]['tcp'][interval]['state']
     # threading.Timer(10, nmapUDP(self,target, interval, spoof, source, randomize)).start()


  def nmapTCP(self,target, interval, spoof, source, randomize, rate):
    # -r DONT RANDOMIZE
    time.sleep(random.randint(2, 10))
    scan_object = nmap.PortScanner()
    if spoof:
      if randomize:
        parameters = '--min-rate ' + rate + ' -e eth0 -S ' + str(source)
      # scan_object.scan(target,interval, arguments = '-r --min-rate 700 -e eth0 -S 141.85.161.236')
      else:
        parameters = '-r --min-rate ' + rate + ' -e eth0 -S ' + str(source)
        # scan_object.scan(target,interval, arguments = '-r --min-rate 700 -e eth0 -S 141.85.161.236')
    else:
      if randomize:
        parameters = '--min-rate ' + rate + ' -e eth0 '
      # scan_object.scan(target,interval, arguments = '--min-rate 700 -e eth0')
      else:
        parameters = '-r --min-rate ' + rate + ' -e eth0 '
        # scan_object.scan(target,interval, arguments = '-r --min-rate 700 -e eth0')
    scan_object.scan(target, interval, arguments=parameters)
    #scan_object.stop() stop thread
    # print scan_object.command_line()
    #state = scan_object[target]['tcp'][interval]['state']
    #threading.Timer(10, self.nmapTCP(target, interval, spoof, source, randomize, rate)).start()


  def generateTraffic(self,target, type, spoof, source, randomize, intervals, nb_bots, rate, scan_interval):
	
	#if self.start_scan == True:
		#while self.start_scan.get():

			print('Repetition')
			for contor in range(int(nb_bots)):
				if type == "TCP":
					t = threading.Thread(target=self.nmapTCP, args=(target, str(intervals[contor]), spoof, source[contor], randomize, rate))
				else:
					t = threading.Thread(target=self.nmapUDP, args=(target, str(intervals[contor]), spoof, source[contor], randomize))
		  		# t = threading.Thread(target = nmapScan, args = ('141.85.161.129', '22-80'))
				t.start()
				print contor
			#self.window.after(int(scan_interval), self.generateTraffic(target, type, spoof, source, randomize, intervals, nb_bots, rate, scan_interval))


root = Tk()
root.withdraw()
BotnetSynthesizer(root)
root.mainloop()
