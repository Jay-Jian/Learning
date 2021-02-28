import wx
import wx.xrc
import test
import codecs

class mywin(test.MyFrame4):
	# status=False
	i=2
	def xxx ( self, event ):
		# global w2
		self.i=(self.i%2)+1
		print(self.i)
		with codecs.open(str(self.i)+".ico","rb") as f:
			self.m_bitmap1.SetBitmap(wx.Bitmap(wx.Image(f,wx.BITMAP_TYPE_ICO)))

	def Click1 ( self, event ):
		file=wx.FileSelector(
			"請選擇檔案",
			wildcard="python檔案|*.py",
			flags=wx.FD_OPEN
		)
		self.m_textCtrl2.Setvalue(file)		

		# self.m_timer1.Start(3000)
		# self.m_textCtrl2.Enabled=False
		# wx.MessageBox("test")
		# self.m_staticText1.SetLabel("123")
		# wx.MessageBox(str(self.m_comboBox1.GetValue())
		# self.m_choice1.Clear()
		# wx.MessageBox(str(self.m_choice1.GetSelection()))
		# wx.MessageBox(str(self.m_filePicker1.GetPath()))
		# self.m_hyperlink1.SetURL("https://www.google.com/")

		# self.m_grid2.AppendCols(7)
		# self.m_grid2.AppendRows(7)
		#AppendCols/AppendRows 新增欄列

		# self.m_grid2.SetColLabelValue(0,"ABC")
		# self.m_grid2.SetRowLabelValue(0,"999")
		#SetColLabelValue/SetRowLabelValue 修改欄列名稱

		# self.m_grid2.SetCellValue(0,0,"zzzz")#SetCellValue 修改值定欄位的值

		# self.m_grid2.SetSize(500,300)#調整表格寬、高
		# if self.status==False:
		# 	w2.Show()
		# 	self.status=True
		# else:
		# 	w2.Hide()
		# 	self.status=False



p=wx.App()#建立應用
w=mywin(None)#電腦視窗中支持子母視窗，目前不需要。必須要給一個空值【None】避免錯誤。
w.Show()#顯示視窗
w.SetTitle("123")
# w2=test.MyFrame11(None)

# for i in range(1,10,1):
# 	w.m_choice1.Append(str(i)) #選單加入i值
p.MainLoop()