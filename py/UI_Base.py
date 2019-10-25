# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"QRCode Geno 1.0 - Created by Waseem S. (Diamond Star)", pos = wx.DefaultPosition, size = wx.Size( 378,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )
		
		gSizer2 = wx.GridSizer( 5, 0, 0, 0 )
		
		self.lb1 = wx.StaticText( self, wx.ID_ANY, u"Welcome to QR Code Geno\nIt enables you to encode a text tnto a QR Code\n\nEnter a text to encode.\n(Max length is 200 characters)", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
		self.lb1.Wrap( -1 )
		self.lb1.SetFont( wx.Font( 11, 74, 90, 90, False, "Arial" ) )
		
		gSizer2.Add( self.lb1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtBox = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,70 ), wx.TE_MULTILINE )
		self.txtBox.SetMaxLength( 200 ) 
		gSizer2.Add( self.txtBox, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.btnGen = wx.Button( self, wx.ID_ANY, u"Generate Code", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnGen, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.imgQR = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 250,250 ), wx.ALWAYS_SHOW_SB )
		self.imgQR.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		gSizer2.Add( self.imgQR, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnExit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.btnExit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_BOTTOM, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnGen.Bind( wx.EVT_BUTTON, self.GenQR )
		self.btnExit.Bind( wx.EVT_BUTTON, self.Exit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def GenQR( self, event ):
		event.Skip()
	
	def Exit( self, event ):
		event.Skip()
	

