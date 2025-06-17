class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, value):
        self._major = value

    @property
    def diemTB(self):
        return self._diemTB

    @diemTB.setter
    def diemTB(self, value):
        self._diemTB = value

    @property
    def hocLuc(self):
        return self._hocLuc

    @hocLuc.setter
    def hocLuc(self, value):
        self._hocLuc = value