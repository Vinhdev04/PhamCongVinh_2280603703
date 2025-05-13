from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = self.listSinhVien[0].id  # Fixed the colon issue
            for sv in self.listSinhVien:
                if maxId < sv.id:
                    maxId = sv.id
            maxId += 1  # Fix the indentation of maxId increment
        return maxId
    
    def soLuongSinhVien(self):
        return len(self.listSinhVien)  # Use len() instead of __len__()
    
    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)  # Fixed variable names
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)
        
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv != None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap nganh hoc sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv.name = name  # Update existing student info, no need to create new object
            sv.sex = sex
            sv.major = major
            sv.diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Khong tim thay sinh vien co ID = {} khong ton tai.".format(ID))
    
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x.diemTB, reverse=False)
    
    def findByID(self, ID):
        searchResult = None
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if sv.id == ID:
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:
            for sv in self.listSinhVien:
                if keyword.upper() in sv.name.upper():
                    listSV.append(sv)
        return listSV  # Fixed return statement typo
    
    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if sv != None:
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv.diemTB >= 8:
            sv.hocLuc = "Gioi"
        elif sv.diemTB >= 6.5:
            sv.hocLuc = "Kha"
        elif sv.diemTB >= 5:
            sv.hocLuc = "Trung Binh"
        else:
            sv.hocLuc = "Yeu"
            
    def showList(self, listSV):
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        if len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocLuc))
        print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien
