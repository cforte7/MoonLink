from PyQt4 import QtGui
import sys



class Window(QtGui.QWidget):
	def __init__(self):
		super(example,self).__init__()
		self.initUI()


'''
def main():
	app = QtGui.QApplication(sys.argv)
	w = QtGui.QWidget()
	w.resize(500,200)
	w.move(200,200)  #Set starting location
	w.setWindowTitle('MoonLink') #Set Title
	w.show() #Activate Window showing on screen
	sys.exit(app.exec_()) 

if __name__ == '__main__':
	main()
'''