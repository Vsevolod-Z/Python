from StringFormatter import*
import wx

class StringFormatterApp(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'StringFormatterApp', size = (400, 300))
        panel = wx.Panel(self, -1)
        self.SetBackgroundColour('YELLOW')
        wx.StaticText(panel, -1, 'Строка:', pos = (5, 22))
        self._input_text = wx.TextCtrl(panel, -1, '', size = (300, -1), pos = (70, 20))
        wx.StaticText(panel, -1, 'Результат:', pos = (5, 232))
        self._result_text = wx.TextCtrl(panel, -1, '', size = (300, -1), pos = (70, 230))

        self._delete_check = wx.CheckBox(panel, -1, 'Удалить слова размером меньше', (70, 60), (210, 20))
        self._spin = wx.SpinCtrl(panel, -1, "", (285, 60), (40, 20))
        self._spin.SetRange(1, 10)
        self._spin.SetValue(5)
        wx.StaticText(panel, -1, "букв", pos=(330, 62))

        self._replace_check = wx.CheckBox(panel, -1,'Заменить все цифры на *', (70, 80), (220, 20))
        self._insert_check = wx.CheckBox(panel, -1,'Вставить по пробелу между символами', (70, 100), (280, 20))

        self._sort_check = wx.CheckBox(panel, -1, 'Сортировать слова в строке', (70, 120), (220, 20))
        self.radio_by_size = wx.RadioButton(panel, -1, 'По размеру', (100, 140), (150, 20))
        self.radio_by_alp = wx.RadioButton(panel, -1, 'Лексикографически', (100, 160), (150, 20))
        self.radio_by_size.SetValue(True)
        self.radio_by_size.Disable()
        self.radio_by_alp.Disable()

        format_btn = wx.Button(panel, -1, 'Форматировать', size = (300, 30), pos = (70, 190))
        self.Bind(wx.EVT_BUTTON, self.on_format_click, format_btn)
        self.Bind(wx.EVT_CHECKBOX, self.sort_check, self._sort_check)

        
    def sort_check(self, event):
        if self._sort_check.IsChecked():
            self.radio_by_size.Enable()
            self.radio_by_alp.Enable()
        else:
            self.radio_by_size.Disable()
            self.radio_by_alp.Disable()


    def on_format_click(self, event):
        result = self._input_text.Value

        if self._sort_check.IsChecked():
            if self.radio_by_size.GetValue():
                result = StringFormatter.sort_size(result) 
            else:
                result = StringFormatter.sort_alphabet(result)

        if self._delete_check.IsChecked():
            result = StringFormatter.del_word(result, int(self._spin.Value))

        if self._replace_check.IsChecked():
            result = StringFormatter.replace_digit(result)

        if self._insert_check.IsChecked():
            result = StringFormatter.insert_space(result)

        self._result_text.Value = result