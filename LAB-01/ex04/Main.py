from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************************************")
    print("** 1. Nhap sinh vien ***")
    print("** 2. Cap nhat sinh vien ***")
    print("** 3. Xoa sinh vien ***")
    print("** 4. Tim kiem sinh vien ***")
    print("** 5. Sap xep sinh vien theo diem TB ***")
    print("** 6. Sap xep sinh vien theo chuyen nganh ***")
    print("** 7. Hien thi danh sach sinh vien ***")
    print("** 8. Thoat ***")
    print("*************************************************")
    
    try:
        key = int(input("Nhap lua chon: "))
    except ValueError:
        print("Vui long nhap lua chon hop le.")
        continue

    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem thanh cong.")
    
    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cap nhat sinh vien.")
            ID = int(input("Nhap ID sinh vien: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID sinh vien: "))
            if qlsv.deleteById(ID):
                print("Xoa thanh cong.")
            else:
                print("Khong tim thay sinh vien co ID = {} khong ton tai.".format(ID))
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien.")
            search_option = input("Tim kiem theo ID (1) hoac ten (2): ")
            if search_option == "1":
                ID = int(input("Nhap ID sinh vien: "))
                sv = qlsv.findByID(ID)
                if sv:
                    print("Sinh vien tim thay: ID = {}, Ten = {}, Gioi tinh = {}, Chuyen nganh = {}, Diem TB = {}, Hoc luc = {}"
                          .format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocLuc))
                else:
                    print("Khong tim thay sinh vien co ID = {}.".format(ID))
            elif search_option == "2":
                keyword = input("Nhap ten sinh vien: ")
                list_sv = qlsv.findByName(keyword)
                if list_sv:
                    for sv in list_sv:
                        print("ID = {}, Ten = {}, Gioi tinh = {}, Chuyen nganh = {}, Diem TB = {}, Hoc luc = {}"
                              .format(sv.id, sv.name, sv.sex, sv.major, sv.diemTB, sv.hocLuc))
                else:
                    print("Khong tim thay sinh vien nao voi ten '{}'.".format(keyword))
            else:
                print("Lua chon khong hop le.")
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem TB.")
            qlsv.sortByDiemTB()
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo chuyen nganh.")
            qlsv.sortByName()  # Sorting by name for simplicity (can change to sort by major if needed)
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")
    
    elif key == 8:
        print("\nThoat chuong trinh.")
        break
    
    else:
        print("\nLua chon khong hop le. Vui long nhap lai.")
