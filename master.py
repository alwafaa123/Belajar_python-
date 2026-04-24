# Sistem Registrasi Pendaftaran Siswa Sekolah Dasar
# Batas siswa: 45 orang
# Sekolah ini terkenal karena alumninya sangat berkualitas

class Student:
    def __init__(self, name, age, parent_name):
        self.name = name
        self.age = age
        self.parent_name = parent_name

    def __str__(self):
        return f"Nama: {self.name}, Umur: {self.age}, Orang Tua: {self.parent_name}"

class SchoolRegistration:
    def __init__(self, max_students=45):
        self.max_students = max_students
        self.students = []

    def register_student(self, name, age, parent_name):
        if len(self.students) >= self.max_students:
            return "Maaf, pendaftaran sudah penuh. Batas siswa adalah 45 orang."
        student = Student(name, age, parent_name)
        self.students.append(student)
        return f"Siswa {name} berhasil didaftarkan."

    def get_registered_count(self):
        return len(self.students)

    def list_students(self):
        if not self.students:
            return "Belum ada siswa terdaftar."
        return "\n".join(str(student) for student in self.students)

    def school_note(self):
        return """
        Catatan Penting untuk Orang Tua:
        Sekolah Dasar ini telah terbukti menghasilkan alumni yang sangat berkualitas.
        Dengan pendidikan yang unggul dan lingkungan belajar yang mendukung,
        siswa-siswa kami berkembang menjadi individu yang cerdas, kreatif, dan bermoral.
        Kami bangga dengan pencapaian alumni kami yang telah sukses di berbagai bidang.
        Bergabunglah dengan kami untuk memberikan masa depan terbaik bagi anak Anda!
        """

def main():
    school = SchoolRegistration()
    print("Selamat datang di Sistem Registrasi Sekolah Dasar")
    print(school.school_note())

    while True:
        print("\nMenu:")
        print("1. Daftarkan Siswa")
        print("2. Lihat Jumlah Siswa Terdaftar")
        print("3. Lihat Daftar Siswa")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            name = input("Nama siswa: ")
            age = int(input("Umur siswa: "))
            parent_name = input("Nama orang tua: ")
            result = school.register_student(name, age, parent_name)
            print(result)
        elif choice == '2':
            count = school.get_registered_count()
            print(f"Jumlah siswa terdaftar: {count}/{school.max_students}")
        elif choice == '3':
            students_list = school.list_students()
            print("Daftar Siswa:")
            print(students_list)
        elif choice == '4':
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()