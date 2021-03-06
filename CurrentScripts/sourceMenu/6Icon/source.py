import xbmc, xbmcgui, serial, binascii, sys, time
 
#get actioncodes from keymap.xml
ACTION_NAV_BACK = 92
ACTION_PREVIOUS_MENU = 10
ACTION_BACKSPACE = 110
 
class MainClass(xbmcgui.WindowDialog):
	def __init__(self):
		
		#background
		self.addControl(xbmcgui.ControlImage(277,200,710,240, '/home/vader/.xbmc/scripts/sourceMenu/customIconPanel.png'))
		#Predefined Text
		#Select an Input Text
		self.strActionInfo = xbmcgui.ControlLabel(580, 205, 700, 200, 'Select a Display', 'font13', '0xFFFFFFFF')
		self.addControl(self.strActionInfo)

		#Displays left TV current source
		self.strLeftInfo = xbmcgui.ControlLabel(330, 235, 200, 200, 'Current:', 'font13', '0xFFFFFFFF')
		self.addControl(self.strLeftInfo)
		self.strLeftSourceInfo = xbmcgui.ControlLabel(400, 235, 200, 200, 'Checking...', 'font13', '0xFFFFFFFF')
		self.addControl(self.strLeftSourceInfo)
		self.getSourceInput(self.strLeftSourceInfo, '\x81')
		self.strLeft = xbmcgui.ControlLabel(400, 410, 200, 200, 'Left TV', 'font13', '0xFFFFFFFF')
		self.addControl(self.strLeft)                

		#Displays Projector current source
		self.strMiddleInfo = xbmcgui.ControlLabel(535, 235, 200, 200, 'Current:', 'font13', '0xFFFFFFFF')
		self.addControl(self.strMiddleInfo)
		self.strMiddleSourceInfo = xbmcgui.ControlLabel(605, 235, 200, 200, 'Checking...', 'font13', '0xFFFFFFFF0')
		self.addControl(self.strMiddleSourceInfo)
		self.getSourceInput(self.strMiddleSourceInfo, '\x82')
		self.strMiddle = xbmcgui.ControlLabel(605, 410, 200, 200, 'Projector', 'font13', '0xFFFFFFFF')
		self.addControl(self.strMiddle)
                                
		#Displays Right TV current source
		self.strRightInfo = xbmcgui.ControlLabel(740, 235, 200, 200, 'Current:', 'font13', '0xFFFFFFFF')
		self.addControl(self.strRightInfo)
		self.strRightSourceInfo = xbmcgui.ControlLabel(810, 235, 200, 200, 'Checking...', 'font13', '0xFFFFFFFF')
		self.addControl(self.strRightSourceInfo)
		self.getSourceInput(self.strRightSourceInfo, '\x83')
		self.strRight = xbmcgui.ControlLabel(810, 410, 200, 200, 'Right TV', 'font13', '0xFFFFFFFF')
		self.addControl(self.strRight)    
                    
		#Location & size of source buttons 
		self.leftSource = xbmcgui.ControlButton(333, 260, 200, 150, "", focusTexture="/home/vader/.xbmc/scripts/sourceMenu/FTTV.jpg", noFocusTexture="/home/vader/.xbmc/scripts/sourceMenu/tv.jpg", textOffsetY=20, textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.leftSource)
		
		self.projectorSource = xbmcgui.ControlButton(533, 260, 200, 150, "", focusTexture="/home/vader/.xbmc/scripts/sourceMenu/FTprojector.jpg", noFocusTexture="/home/vader/.xbmc/scripts/sourceMenu/projector.jpg", textOffsetY=20, textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.projectorSource)
		
		self.rightSource = xbmcgui.ControlButton(733, 260, 200, 150, "", focusTexture="/home/vader/.xbmc/scripts/sourceMenu/FTTV.jpg", noFocusTexture="/home/vader/.xbmc/scripts/sourceMenu/tv.jpg", textOffsetY=20, textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.rightSource)
		
				
		self.allDisplays = xbmcgui.ControlButton(280, 260, 45, 120, "", focusTexture="/home/vader/.xbmc/scripts/sourceMenu/FTallButton.png", noFocusTexture="/home/vader/.xbmc/scripts/sourceMenu/allButton.png", textOffsetY=20, textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.allDisplays)
		
				
		self.reset = xbmcgui.ControlButton(940, 260, 45, 120, "", focusTexture="/home/vader/.xbmc/scripts/sourceMenu/FTresetButton.png", noFocusTexture="/home/vader/.xbmc/scripts/sourceMenu/resetButton.png",textOffsetY=20, textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.reset)
		#Start flashing icon on Projector Icon
		self.setFocus(self.projectorSource)
		
		#Left TV Button can make the following moves	
		self.leftSource.controlLeft(self.allDisplays)		
		self.leftSource.controlRight(self.projectorSource)
		
		#Projector TV Button can make the following moves
		self.projectorSource.controlLeft(self.leftSource)
		self.projectorSource.controlRight(self.rightSource)
		
		#Right TV Button can make the following moves	
		self.rightSource.controlLeft(self.projectorSource)
		self.rightSource.controlRight(self.reset)
				
		#All Displays Button can make the following moves
		self.allDisplays.controlLeft(self.reset)
		self.allDisplays.controlRight(self.leftSource)
		
		#Reset Button can make the following moves	
		self.reset.controlLeft(self.rightSource)
		self.reset.controlRight(self.allDisplays)
	
	def onAction(self, action):
		if action == ACTION_PREVIOUS_MENU:
			self.close()
		elif action == ACTION_NAV_BACK:
			self.close()
		elif action == ACTION_BACKSPACE:
			self.close()	
			
	def onControl(self, control):
		if control == self.leftSource:
			self.setFocus(self.leftSource)	
            #self.outputNameInfo.setLabel('Left TV current source:')
			popup = singleChildClass()
			popup.setOutputInfo('Left TV:', '\x81')
			popup .doModal()
			del popup
			self.getSourceInput(self.strLeftSourceInfo, '\x81')
		elif control == self.projectorSource:
            #self.outputNameInfo.setLabel('Projector current source:')		
			popup = singleChildClass()
			popup.setOutputInfo('Projector:','\x82')
			popup .doModal()
			del popup
			self.getSourceInput(self.strMiddleSourceInfo, '\x82')
		elif control == self.rightSource:
            #self.outputNameInfo.setLabel('Right TV current source:')		
			self.setFocus(self.rightSource)			
			popup = singleChildClass()
			popup.setOutputInfo('Right TV:', '\x83')
			popup .doModal()
			del popup
			self.getSourceInput(self.strRightSourceInfo, '\x83')
		elif control == self.allDisplays:
			self.setFocus(self.allDisplays)
			#figure out the single source children first
			popup = multiChildClass()
			popup.setOutputInfo('All Displays')
			popup .doModal()
			del popup
			self.getSourceInput(self.strLeftSourceInfo, '\x81')
			self.getSourceInput(self.strMiddleSourceInfo, '\x82')
			self.getSourceInput(self.strRightSourceInfo, '\x83')
		elif control == self.reset:
			self.setFocus(self.reset)
			#special reset calls
			xbmc.executebuiltin("Notification(Reset, Setting sources to default configuration...)")
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x82\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x85\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x81\x83\x81')
			self.getSourceInput(self.strLeftSourceInfo, '\x81')
			self.getSourceInput(self.strMiddleSourceInfo, '\x82')
			self.getSourceInput(self.strRightSourceInfo, '\x83')

	def getSourceInput(self, label, outputNumber):
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
		ser.flushInput()
		ser.write('\x05\x80' + outputNumber + '\x81')
		ser.read(2)
		out = ser.read()
		ser.close()
		foo = binascii.b2a_qp(out)
		source = foo[2]
		if source == '1': 
			label.setLabel('WiDi 1')
		elif source == '2': 
			label.setLabel('Apple TV 1')
		elif source == '3':
			label.setLabel('WiDi 2')
		elif source == '4':
			label.setLabel('Apple TV 2')
		elif source == '5':
			label.setLabel('VADER')
		else:
			label.setLabel('UNKNOWN')
		
class singleChildClass(xbmcgui.WindowDialog):
	def __init__(self):
		#background
		self.addControl(xbmcgui.ControlImage(0,0,1275,750, '/home/vader/.xbmc/scripts/sourceMenu/6Icon/sourceBackground.jpg'))
		#Select an Input Text
		self.strActionInfo = xbmcgui.ControlLabel(452, 185, 700, 200, 'Select an Input', 'Font_MainClassic', '0xFFFFFFFF')
		self.addControl(self.strActionInfo)
		self.outputName = ''
		self.outputNumber = ''

		#Displays current source
		self.outputNameInfo = xbmcgui.ControlLabel(63, 325, 200, 200, self.outputName, 'font13', '0xFF000000')
		self.addControl(self.outputNameInfo)
		self.strSourceInfo = xbmcgui.ControlLabel(140, 325, 200, 200, 'Checking...', 'font13', '0xFF000000')
		self.addControl(self.strSourceInfo)
		#Location and size of buttons
		self.button0 = xbmcgui.ControlButton(340, 260, 200, 150, "",focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTvaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
		self.addControl(self.button0)
	
		self.button1 = xbmcgui.ControlButton(542, 260, 200, 150, "", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTwidiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button1)

		self.button2 = xbmcgui.ControlButton(742, 260, 200, 150, "APPLE TV 1", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTappleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button2)

		self.button3 = xbmcgui.ControlButton(340, 410, 200, 150, "", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTwidiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button3)

		self.button4 = xbmcgui.ControlButton(542, 410, 200, 150, "APPLE TV 2", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTappleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button4)	

		self.button5 = xbmcgui.ControlButton(744, 412, 196, 145, "CANCEL", textOffsetX=57, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/cancelButton.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTcancelButton.jpg', textColor='0xFF000000',  focusedColor='0xFFFFFFFF')
		self.addControl(self.button5)

		#Start flashing icon on button0
		self.setFocus(self.button0)
		
		#VADER Button can make the following moves	
		self.button0.controlDown(self.button3)
		self.button0.controlRight(self.button1)
		self.button0.controlLeft(self.button2)
		self.button0.controlUp(self.button3)

		#WIDI 1 Button can make the following moves
		self.button1.controlDown(self.button4)
		self.button1.controlRight(self.button2)
		self.button1.controlLeft(self.button0)
		self.button1.controlUp(self.button4)

		#Apple TV 1 Button can make the following moves	
		self.button2.controlDown(self.button5)
		self.button2.controlRight(self.button0)
		self.button2.controlLeft(self.button1)
		self.button2.controlUp(self.button5)

		#WIDI 2 Button can make the following moves	
		self.button3.controlDown(self.button0)
		self.button3.controlRight(self.button4)
		self.button3.controlLeft(self.button5)	
		self.button3.controlUp(self.button0)	

		#Apple TV 2 Button can make the following moves	
		self.button4.controlDown(self.button1)
		self.button4.controlRight(self.button5)
		self.button4.controlLeft(self.button3)
		self.button4.controlUp(self.button1)

		#Cancel button
		self.button5.controlDown(self.button2)
		self.button5.controlRight(self.button3)
		self.button5.controlLeft(self.button4)
		self.button5.controlUp(self.button2)
		
	def setOutputInfo(self, outputName, outputNumber):
		#Setup output info
		self.outputName = outputName
		self.outputNumber = outputNumber
		self.outputNameInfo.setLabel(outputName)
		self.getSourceInput(self.strSourceInfo)

	def onControl(self, control):
		if control == self.button0:
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x85' + self.outputNumber + '\x81')
			self.message('Switching ' + self.outputName + ' to VADER')
			self.getSourceInput(self.strSourceInfo)
		if control == self.button1:
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x81' + self.outputNumber + '\x81')
			self.message('Switching ' + self.outputName + ' to WiDi 1')
			self.getSourceInput(self.strSourceInfo)
		if control == self.button2:
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x82' + self.outputNumber + '\x81')
			self.message('Switching ' + self.outputName + ' to Apple TV 1')
			self.getSourceInput(self.strSourceInfo)
		if control == self.button3:
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x83' + self.outputNumber + '\x81')
			self.message('Switching ' + self.outputName + ' to WiDi 2')
			self.getSourceInput(self.strSourceInfo)
		if control == self.button4:
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x84' + self.outputNumber + '\x81')
			self.message('Switching ' + self.outputName + ' to Apple TV 2')
			self.getSourceInput(self.strSourceInfo)
		if control == self.button5:
			self.close()
		  
	def getSourceInput(self, label):
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
		ser.flushInput()
		ser.write('\x05\x80' + self.outputNumber + '\x81')
		ser.read(2)
		out = ser.read()
		ser.close()
		foo = binascii.b2a_qp(out)
		source = foo[2]
		if source == '1':
			self.button6 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg')
			self.addControl(self.button6)    
			label.setLabel('WiDi 1')
		elif source == '2':
			self.button6 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg')
			self.addControl(self.button6)   
			label.setLabel('Apple TV 1')
		elif source == '3':
			self.button6 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg')
			self.addControl(self.button6)    
			label.setLabel('WiDi 2')
		elif source == '4':
			self.button6 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg')
			self.addControl(self.button6)
			label.setLabel('Apple TV 2')
		elif source == '5':
			self.button6 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
			self.addControl(self.button6)
			label.setLabel('VADER')
		else:
			label.setLabel('UNKNOWN')
	
	def message(self, message):
		dialog = xbmcgui.Dialog()
		dialog.ok("Video Source Control", message)
	
	def onAction(self, action):
		if action == ACTION_PREVIOUS_MENU:
			self.close()				
		elif action == ACTION_NAV_BACK:
			self.close()	
		elif action == ACTION_BACKSPACE:
			self.close()

class multiChildClass(xbmcgui.WindowDialog):
	def __init__(self):
		#background
		self.addControl(xbmcgui.ControlImage(0,0,1275,750, '/home/vader/.xbmc/scripts/sourceMenu/6Icon/sourceBackground.jpg'))

		#Select an Input Text
		self.strActionInfo = xbmcgui.ControlLabel(452, 185, 700, 200, 'Select an Input', 'Font_MainClassic', '0xFFFFFFFF')
		self.addControl(self.strActionInfo)
		self.outputName = ''
		self.outputNumber = ''

		#Displays current source 1
		self.outputNameInfo1 = xbmcgui.ControlLabel(63, 195, 200, 200, 'Left TV - ', 'font13', '0xFF000000')
		self.addControl(self.outputNameInfo1)
		self.strSourceInfo1 = xbmcgui.ControlLabel(130, 195, 200, 200, 'Checking...', 'font13', '0xFF000000')
		self.addControl(self.strSourceInfo1)
		
		#Displays current source 2
		self.outputNameInfo2 = xbmcgui.ControlLabel(63, 325, 200, 200, 'Projector - ', 'font13', '0xFF000000')
		self.addControl(self.outputNameInfo2)
		self.strSourceInfo2 = xbmcgui.ControlLabel(147, 325, 200, 200, 'Checking...', 'font13', '0xFF000000')
		self.addControl(self.strSourceInfo2)
		
		#Displays current source 3
		self.outputNameInfo3 = xbmcgui.ControlLabel(63, 455, 200, 200, 'Right TV - ', 'font13', '0xFF000000')
		self.addControl(self.outputNameInfo3)
		self.strSourceInfo3 = xbmcgui.ControlLabel(140, 455, 200, 200, 'Checking...', 'font13', '0xFF000000')
		self.addControl(self.strSourceInfo3)
		
		#Location and size of buttons
		self.button0 = xbmcgui.ControlButton(340, 260, 200, 150, "",focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTvaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
		self.addControl(self.button0)
	
		self.button1 = xbmcgui.ControlButton(542, 260, 200, 150, "", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTwidiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button1)

		self.button2 = xbmcgui.ControlButton(742, 260, 200, 150, "APPLE TV 1", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTappleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button2)

		self.button3 = xbmcgui.ControlButton(340, 410, 200, 150, "", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTwidiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')
		self.addControl(self.button3)

		self.button4 = xbmcgui.ControlButton(542, 410, 200, 150, "APPLE TV 2", textOffsetX=5, textOffsetY=10, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTappleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg',textColor='0xFF000000', focusedColor='0xFFFFFFFF')

		self.addControl(self.button4)	

		self.button5 = xbmcgui.ControlButton(744, 412, 196, 145, "CANCEL", textOffsetX=57, focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/cancelButton.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/FTcancelButton.jpg', textColor='0xFF000000',  focusedColor='0xFFFFFFFF')
		self.addControl(self.button5)

		#Start flashing icon on button0
		self.setFocus(self.button0)
		
		#VADER Button can make the following moves	
		self.button0.controlDown(self.button3)
		self.button0.controlRight(self.button1)
		self.button0.controlLeft(self.button2)
		self.button0.controlUp(self.button3)

		#WIDI 1 Button can make the following moves
		self.button1.controlDown(self.button4)
		self.button1.controlRight(self.button2)
		self.button1.controlLeft(self.button0)
		self.button1.controlUp(self.button4)

		#Apple TV 1 Button can make the following moves	
		self.button2.controlDown(self.button5)
		self.button2.controlRight(self.button0)
		self.button2.controlLeft(self.button1)
		self.button2.controlUp(self.button5)

		#WIDI 2 Button can make the following moves	
		self.button3.controlDown(self.button0)
		self.button3.controlRight(self.button4)
		self.button3.controlLeft(self.button5)	
		self.button3.controlUp(self.button0)	

		#Apple TV 2 Button can make the following moves	
		self.button4.controlDown(self.button1)
		self.button4.controlRight(self.button5)
		self.button4.controlLeft(self.button3)
		self.button4.controlUp(self.button1)

		#Cancel button
		self.button5.controlDown(self.button2)
		self.button5.controlRight(self.button3)
		self.button5.controlLeft(self.button4)
		self.button5.controlUp(self.button2)
		
	def setOutputInfo(self, outputName):
		#Setup output info
		self.outputName = outputName
		self.getSourceInput()

	def onControl(self, control):
		if control == self.button0:
			self.message('Switching ' + self.outputName + ' to VADER')
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x85\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x85\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x85\x83\x81')
			self.getSourceInput()
		if control == self.button1:
			self.message('Switching ' + self.outputName + ' to WiDi 1')
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x81\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x81\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x81\x83\x81')
			self.getSourceInput()
		if control == self.button2:
			self.message('Switching ' + self.outputName + ' to Apple TV 1')
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x82\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x82\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x82\x83\x81')
			self.getSourceInput()
		if control == self.button3:
			self.message('Switching ' + self.outputName + ' to WiDi 2')
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x83\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x83\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x83\x83\x81')
			self.getSourceInput()
		if control == self.button4:
			self.message('Switching ' + self.outputName + ' to Apple TV 2')
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x84\x81\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x84\x82\x81')
			time.sleep(0.02)
			serial.Serial('/dev/ttyUSB0', 9600, timeout=1).write('\x01\x84\x83\x81')
			self.getSourceInput()
		if control == self.button5:
			self.close()
		  
	def getSourceInput(self):
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
		ser.flushInput()
		ser.write('\x05\x80\x81\x81')
		ser.read(2)
		out = ser.read()
		ser.close()
		foo = binascii.b2a_qp(out)
		source = foo[2]
		if source == '1':
			self.button6 = xbmcgui.ControlButton(63, 220, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg')
			self.addControl(self.button6)    
			self.strSourceInfo1.setLabel('WiDi 1')
		elif source == '2':
			self.button6 = xbmcgui.ControlButton(63, 220, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg')
			self.addControl(self.button6)   
			self.strSourceInfo1.setLabel('Apple TV 1')
		elif source == '3':
			self.button6 = xbmcgui.ControlButton(63, 220, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg')
			self.addControl(self.button6)    
			self.strSourceInfo1.setLabel('WiDi 2')
		elif source == '4':
			self.button6 = xbmcgui.ControlButton(63, 220, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg')
			self.addControl(self.button6)
			self.strSourceInfo1.setLabel('Apple TV 2')
		elif source == '5':
			self.button6 = xbmcgui.ControlButton(63, 220, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
			self.addControl(self.button6)
			self.strSourceInfo1.setLabel('VADER')
		else:
			self.strSourceInfo1.setLabel('UNKNOWN')
		
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
		ser.flushInput()
		ser.write('\x05\x80\x82\x81')
		ser.read(2)
		out = ser.read()
		ser.close()
		foo = binascii.b2a_qp(out)
		source = foo[2]
		if source == '1':
			self.button7 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg')
			self.addControl(self.button7)    
			self.strSourceInfo2.setLabel('WiDi 1')
		elif source == '2':
			self.button7 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg')
			self.addControl(self.button7)   
			self.strSourceInfo2.setLabel('Apple TV 1')
		elif source == '3':
			self.button7 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg')
			self.addControl(self.button7)    
			self.strSourceInfo2.setLabel('WiDi 2')
		elif source == '4':
			self.button7 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg')
			self.addControl(self.button7)
			self.strSourceInfo2.setLabel('Apple TV 2')
		elif source == '5':
			self.button7 = xbmcgui.ControlButton(63, 350, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
			self.addControl(self.button7)
			self.strSourceInfo2.setLabel('VADER')
		else:
			self.strSourceInfo2.setLabel('UNKNOWN')
			
		ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
		ser.flushInput()
		ser.write('\x05\x80\x83\x81')
		ser.read(2)
		out = ser.read()
		ser.close()
		foo = binascii.b2a_qp(out)
		source = foo[2]
		if source == '1':
			self.button8 = xbmcgui.ControlButton(63, 480, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton1.jpg')
			self.addControl(self.button8)    
			self.strSourceInfo3.setLabel('WiDi 1')
		elif source == '2':
			self.button8 = xbmcgui.ControlButton(63, 480, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV1.jpg')
			self.addControl(self.button8)   
			self.strSourceInfo3.setLabel('Apple TV 1')
		elif source == '3':
			self.button8 = xbmcgui.ControlButton(63, 480, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/widiButton2.jpg')
			self.addControl(self.button8)    
			self.strSourceInfo3.setLabel('WiDi 2')
		elif source == '4':
			self.button8 = xbmcgui.ControlButton(63, 480, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/appleTV2.jpg')
			self.addControl(self.button8)
			self.strSourceInfo3.setLabel('Apple TV 2')
		elif source == '5':
			self.button8 = xbmcgui.ControlButton(63, 480, 150, 100, "", focusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg', noFocusTexture='/home/vader/.xbmc/scripts/sourceMenu/6Icon/vaderButton2.jpg')
			self.addControl(self.button8)
			self.strSourceInfo3.setLabel('VADER')
		else:
			self.strSourceInfo3.setLabel('UNKNOWN')
	
	def message(self, message):
		xbmc.executebuiltin('Notification(Video Source Control, ' + message + ')')
	
	def onAction(self, action):
		if action == ACTION_PREVIOUS_MENU:
			self.close()				
		elif action == ACTION_NAV_BACK:
			self.close()	
		elif action == ACTION_BACKSPACE:
			self.close()

mydisplay = MainClass()
mydisplay .doModal()
del mydisplay
