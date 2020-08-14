class State:
    """状態を管理するクラスです
    """

    def __init__(self, name):
        self.__name = name
        self.__trans = []
        self.__froms = []
        self.__fillColor = "#ffffff"
        self.__frameColor = "#000000"
        self.__ini = False
    
    def addTrans(self, dst):
        self.__trans.append(dst)
    
    def addFroms(self, src):
        self.__froms.append(src)
    
    @property
    def name(self):
        return self.__name

    @property
    def trans(self):
        return self.__trans
    
    @property
    def froms(self):
        return self.__froms
    
    @property
    def fillColor(self):
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor):
        self.__fillColor = fillColor
    
    @property
    def frameColor(self):
        return self.__frameColor
    
    @frameColor.setter
    def frameColor(self, frameColor):
        self.__frameColor = frameColor
    
    @property
    def ini(self):
        return self.__ini
    
    @ini.setter
    def ini(self, Info):
        self.__ini = True