import wx
import os

import datetime
import re

class AppTask3(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'AppTask3', size = (1000, 600))

        self._list_box = wx.ListBox(self, style = wx.LB_SINGLE)
        self._status_bar = self.CreateStatusBar(2)
        self._status_bar.SetStatusWidths([-6, -4])
        self.Show(True)

        self.is_exists_log()
        
        menu_open = wx.Menu() 
        open_item = menu_open.Append(wx.ID_OPEN, 'Open')
        menu_log = wx.Menu()
        export_item = menu_log.Append(wx.ID_SAVE, 'Export')
        add_item = menu_log.Append(wx.ID_ADD, 'Add to log')
        view_item = menu_log.Append( wx.ID_ABOUT, 'Show')
        menu_bar = wx.MenuBar()
        menu_bar.Append(menu_open, 'File')  
        menu_bar.Append(menu_log, 'Log')
        self.SetMenuBar(menu_bar)

        self.Bind(wx.EVT_MENU, self.open_file, open_item)
        self.Bind(wx.EVT_MENU, self.export_log, export_item)
        self.Bind(wx.EVT_MENU, self.add_log, add_item)
        self.Bind(wx.EVT_MENU, self.view_log, view_item)

    def open_file(self, e):
        self._dir_name = ' '
        reg = r"(?:[0-9]{3})(?:\.[0-9]+){3}"
        open_dialog = wx.FileDialog(self, 'Choose file', self._dir_name, ' ', '*.*') 
        if open_dialog.ShowModal() == wx.ID_OK:  
            self._file_name = open_dialog.GetFilename()  
            self._dir_name = open_dialog.GetDirectory() 
            path = os.path.join(self._dir_name, self._file_name)
            with open(path) as file:
                data = file.readlines()
                self._list_box.Append('File ' + path + ' was processed ' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S') + ':')
                self._list_box.Append('')
                for i in range(len(data)):
                    parser = re.search(reg,data[i])
                    count = 0
                    while parser!=None:
                        self._list_box.Append('String, ' + str(i+1) + ' position ' + str(parser.regs[0][0] + count + 1) + ': find ' + "«" + parser.group() +  "»")
                        count += parser.regs[0][1]
                        data[i] = data[i][parser.regs[0][1]:]
                        parser = re.search(reg,data[i])
            self._list_box.Append("")
            file_size = str(os.path.getsize(path))[::-1]
            file_size = ''.join([file_size[i] + ' ' if i%3 == 0 else file_size[i]  for i in range(len(file_size))][::-1])
            self._status_bar.SetStatusText('File processed ' + path)
            self._status_bar.SetStatusText(file_size + 'byte', 1)

    def add_log(self, e):
        path = os.path.join(os.getcwd(), 'Task3Log.log')
        with open(path, 'a') as file:
            for line in self._list_box.GetStrings():
                file.write(line + '\n')

    def export_log(self, e):
        self._dir_name = " "
        open_dialog = wx.FileDialog(self, 'Select the file to write to', self._dir_name, ' ', '*.*')  
        if open_dialog.ShowModal() == wx.ID_OK: 
            self._file_name,self._dir_name = open_dialog.GetFilename(), open_dialog.GetDirectory()  
            path = open_dialog.GetPath()
            with open(path, 'w') as file:
                for line in self._list_box.GetStrings():
                    print(line)
                    file.write(line + '\n')

    def view_log(self, e):
        dialog = wx.MessageDialog(self, 'Do you want to open the log, the last data will be lost?', 'Log view', wx.YES_NO)  
        if dialog.ShowModal() == wx.ID_YES:
            self._list_box.Clear()
            path = os.path.join(os.getcwd(), 'Task3Log.log')
            with open(path, "r") as file:
                self._list_box.AppendItems(file.readlines())
            self._status_bar.SetStatusText('Open log')
            self._status_bar.SetStatusText('', 1)
        else:
            dialog.Destroy()

    def is_exists_log(self):
        log_filename = 'Task3Log.log'
        path = os.path.join(os.getcwd(), log_filename)
        if not os.path.exists(path):
            dialog = wx.MessageDialog(self, 'The log file was not found. The file will be created automatically', 'Warning!', wx.OK)  
            dialog.ShowModal()
    