// Superclass untuk golongan masyarakat kampus
class MasyarakatKampus {
    String nama;
    String golongan;
    double gaji;

    public MasyarakatKampus(String nama, String golongan, double gaji) {
        this.nama = nama;
        this.golongan = golongan;
        this.gaji = gaji;
    }

    public void tampilkanInfo() {
        System.out.println("Nama: " + nama);
        System.out.println("Golongan: " + golongan);
        System.out.println("Gaji: " + gaji);
    }
}

// Subclass untuk DOSEN
class Dosen extends MasyarakatKampus {
    public Dosen(String nama, double gaji) {
        super(nama, "DOSEN", gaji);
    }
}

// Subclass untuk STAFF
class Staff extends MasyarakatKampus {
    public Staff(String nama, double gaji) {
        super(nama, "STAFF", gaji);
    }
}

// Subclass untuk Lainnya
class Lainnya extends MasyarakatKampus {
    public Lainnya(String nama, double gaji) {
        super(nama, "LAINNYA", gaji);
    }
}

// Main class untuk menjalankan program
public class Main {
    public static void main(String[] args) {
        // Membuat objek dari masing-masing golongan
        Dosen dosen = new Dosen("Dr. Budi", 8000000);
        Staff staff = new Staff("Siti", 5000000);
        Lainnya lainnya = new Lainnya("John", 3000000);

        // Menampilkan informasi masing-masing objek
        dosen.tampilkanInfo();
        System.out.println();
        staff.tampilkanInfo();
        System.out.println();
        lainnya.tampilkanInfo();
    }
}
