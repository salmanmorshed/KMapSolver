import wx
from solvers import KMapSolver2, KMapSolver3, KMapSolver4


class KMapGui(object):
    map_data = [[]]
    all_vars = ''
    KMapSolver = None
    WindowSize = (0, 0)

    def __init__(self):
        self.frame = wx.Frame(None, -1, "K-Map Solver",
                              style=wx.SYSTEM_MENU|wx.CAPTION|wx.MINIMIZE_BOX|wx.CLOSE_BOX)
        self.panel = wx.Panel(self.frame)
        self.buttons = []
        self.setup_lines()
        self.setup_labels()
        self.setup_buttons()
        self.frame.SetSize(self.WindowSize)
        self.frame.Show()


    def setup_lines(self):
        hln = len(self.map_data) + 2
        vln = len(self.map_data[0]) + 2

        for hl in range(0, hln):
            wx.StaticLine(self.panel, pos=(5, 5 + (50 * hl)), size=((vln - 1) * 50, 2), style=wx.LI_HORIZONTAL)

        for vl in range(0, vln):
            wx.StaticLine(self.panel, pos=(5 + (50 * vl), 5), size=(2, (hln - 1) * 50), style=wx.LI_VERTICAL)

    def setup_labels(self):
        pass

    def setup_buttons(self):
        vln = len(self.map_data[0]) + 2
        calc_btn = wx.Button(self.panel, label='Calculate', pos=((vln * 50 - 30), 5), size=(80, 30))
        reset_btn = wx.Button(self.panel, label='Reset', pos=((vln * 50 - 30), 40), size=(80, 30))
        calc_btn.Bind(wx.EVT_BUTTON, self.show_result)
        reset_btn.Bind(wx.EVT_BUTTON, self.reset)

        for i, row in enumerate(self.map_data):
            q = []
            for j, ele in enumerate(row):
                b = wx.Button(self.panel,
                              id=(100 + i*10 + j),
                              label="0",
                              pos=(60 + (50*j), 60 + (50*i)),
                              size=(40, 40))
                b.Bind(wx.EVT_BUTTON, self.ele_button_clicked)
                q.append(b)
            self.buttons.append(q)

    def ele_button_clicked(self, e):
        ele_id = e.GetId() - 100
        x = ele_id / 10
        y = ele_id % 10
        self.map_data[x][y] = ([1, 2, 0])[int(self.map_data[x][y])]
        self.buttons[x][y].SetLabel(str(self.map_data[x][y]) if self.map_data[x][y] != 2 else 'X')

    def calc_result(self):
        k = self.KMapSolver(self.map_data)
        k.solve()
        return k.get_result()

    def show_result(self, _):
        result = "F({}) = {}".format(self.all_vars, self.calc_result())
        wx.MessageBox(result, 'Result', wx.OK | wx.ICON_INFORMATION)

    def reset(self, _):
        for i, x in enumerate(self.map_data):
            for j, y in enumerate(x):
                self.map_data[i][j] = 0

        for bl in self.buttons:
            for b in bl:
                b.SetLabel('0')


class KMapGui2(KMapGui):
    map_data = [[ 0, 0],
                 [ 0, 0]]
    all_vars = 'A, B'
    KMapSolver = KMapSolver2
    WindowSize = (280, 200)

    def setup_labels(self):
        wx.StaticText(self.panel, label='A\\B', pos=(10, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='0', pos=(10, 60), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='1', pos=(10, 110), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='0', pos=(60, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='1', pos=(110, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)


class KMapGui3(KMapGui):
    map_data = [[ 0, 0, 0, 0],
                 [ 0, 0, 0, 0]]
    all_vars = 'A, B, C'
    KMapSolver = KMapSolver3
    WindowSize = (380, 200)

    def setup_labels(self):
        wx.StaticText(self.panel, label='A\\BC', pos=(10, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='0', pos=(10, 60), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='1', pos=(10, 110), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='00', pos=(60, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='01', pos=(110, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='11', pos=(160, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='10', pos=(210, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)


class KMapGui4(KMapGui):
    map_data = [[ 0, 0, 0, 0],
                 [ 0, 0, 0, 0],
                 [ 0, 0, 0, 0],
                 [ 0, 0, 0, 0]]
    all_vars = 'A, B, C, D'
    KMapSolver = KMapSolver4
    WindowSize = (380, 300)

    def setup_labels(self):
        wx.StaticText(self.panel, label='AB\\CD', pos=(10, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='00', pos=(10, 60), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='01', pos=(10, 110), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='11', pos=(10, 160), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='10', pos=(10, 210), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='00', pos=(60, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='01', pos=(110, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='11', pos=(160, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
        wx.StaticText(self.panel, label='10', pos=(210, 10), size=(40, 40), style=wx.ALIGN_CENTER_VERTICAL)
