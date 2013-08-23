import sublime, sublime_plugin

# fffffff 0x001

TEMPLATE = "dec: {0} hex: {0:#x} bin: {0:0>8b}"
KEY_STATUS = "selection_number_listener_status"

class SelectionNumberListener(sublime_plugin.EventListener):

    def on_selection_modified_async(self, view):
        sel = view.sel()[-1]
        selText = view.substr(sel)
        try:
            num = self.getDeciamlFromText(selText)
            outputStr = self.buildString(num)
            view.set_status(KEY_STATUS, outputStr)
        except:
            view.set_status(KEY_STATUS, "")

    def getDeciamlFromText(self, text):
        for base in [10, 16]:
            try:
                number = int(text, base)
            except ValueError:
                continue
            return number
        raise ValueError()

    def buildString(self, decimal):
        resStr = TEMPLATE.format(decimal)
        return resStr