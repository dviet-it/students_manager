"""
Author: Dang Duc Viet
University: Posts and Telecommunications Institute of Technology
Major: D25 - IT UDU
Project Name: Quản lý sinh viên
Class Code: D25CQCC05-B
Student ID: B25DCCC269
Created: 2025-10-10 12:47
"""


class Student:
    def __init__(self, student_id, name, age, score):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return f"ID: {self.student_id} | Tên: {self.name} | Tuổi: {self.age} | Điểm: {self.score}"


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Nhập ID sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi: "))
        score = float(input("Nhập điểm: "))
        student = Student(student_id, name, age, score)
        self.students.append(student)
        print("✅ Thêm sinh viên thành công!")

    def show_students(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
        else:
            print("\n--- DANH SÁCH SINH VIÊN ---")
            for s in self.students:
                print(s)

    def update_student(self):
        student_id = input("Nhập ID sinh viên cần cập nhật: ")
        for s in self.students:
            if s.student_id == student_id:
                s.name = input("Nhập tên mới: ")
                s.age = int(input("Nhập tuổi mới: "))
                s.score = float(input("Nhập điểm mới: "))
                print("Cập nhật thành công!")
                return
        print("Không tìm thấy sinh viên có ID này.")

    def delete_student(self):
        student_id = input("Nhập ID sinh viên cần xóa: ")
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                print("Xóa thành công!")
                return
        print("Không tìm thấy sinh viên có ID này.")

    def search_student(self):
        keyword = input("Nhập tên hoặc ID sinh viên cần tìm: ").lower()
        found = [s for s in self.students if keyword in s.name.lower() or keyword in s.student_id.lower()]
        if found:
            print("\n--- KẾT QUẢ TÌM KIẾM ---")
            for s in found:
                print(s)
        else:
            print("Không tìm thấy sinh viên.")

    def sort_students(self):
        self.students.sort(key=lambda x: x.score, reverse=True)
        print("Đã sắp xếp sinh viên theo điểm giảm dần.")


def main():
    manager = StudentManager()
    while True:
        print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Cập nhật thông tin")
        print("4. Xóa sinh viên")
        print("5. Tìm kiếm sinh viên")
        print("6. Sắp xếp theo điểm")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.show_students()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "6":
            manager.sort_students()
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()