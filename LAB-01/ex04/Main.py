from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*************************************************")
    print("** 1. Nhập sinh viên ***")
    print("** 2. Cập nhật sinh viên ***")
    print("** 3. Xóa sinh viên ***")
    print("** 4. Tìm kiếm sinh viên theo tên ***")
    print("** 5. Sắp xếp sinh viên theo điểm TB ***")
    print("** 6. Sắp xếp sinh viên theo tên ***")
    print("** 7. Hiển thị danh sách sinh viên ***")
    print("** 8. Thoát ***")
    print("*************************************************")

    try:
        key = int(input("Nhập lựa chọn của bạn: "))
    except ValueError:
        print("Vui lòng nhập lựa chọn hợp lệ.")
        continue

    if key == 1:
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm thành công.")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cập nhật sinh viên.")
            ID = int(input("Nhập ID sinh viên: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xóa sinh viên.")
            ID = int(input("Nhập ID sinh viên: "))
            if qlsv.deleteById(ID):
                print("Xóa thành công.")
            else:
                print("Không tìm thấy sinh viên có ID = {}.".format(ID))
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tìm kiếm sinh viên theo tên")
            print("\nNhâp tên: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showList(searchResult)
         
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sắp xếp sinh viên theo điểm trung bình.")
            qlsv.sortByDiemTB()
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sắp xếp sinh viên theo tên")
            qlsv.sortByName()  # Note: This sorts by name, not major; consider adding sortByMajor if needed
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showList(qlsv.getListSinhVien())
        else:
            print("\nKhông có sinh viên nào trong danh sách!")

    elif key == 8:
        print("\nThoát chương trình.")
        break

    else:
        print("\nLựa chọn không hợp lệ. Vui lòng nhập lại.")