import os
import Widget

class WidgetLoader:

    def __init__(self):
        self.configfilepath = os.path.join(os.pardir, os.path("configs/widgets.conf"))
        self.widgetObjects = []

    def load(self):
        widgetObjects = []
        filepointer = open(self.configfilepath, "r")

        while True:
            line = filepointer.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                break
            line = line.split(',')

            widget = Widget()
            widget.setName(line[0].strip())
            widget.getCode(line[1].strip())
            widget.setPrice(float(line[2].strip()))

            widgetObjects.append(widget)

        filepointer.close()

        self.widgetObjects = widgetObjects

    def getWidgetObjects(self):
        return self.widgetObjects
