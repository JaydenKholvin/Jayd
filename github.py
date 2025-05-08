import datetime

# Fungsi untuk menampilkan menu utama
def display_menu():
    print("\n=== Aplikasi Kasir Mini ===")
    print("1. Tambah Barang")
    print("2. Lihat Keranjang Belanja")
    print("3. Hapus Barang dari Keranjang")
    print("4. Hitung Total Belanja")
    print("5. Simpan Transaksi")
    print("6. Lihat Riwayat Transaksi")
    print("7. Keluar")

# Fungsi untuk menambahkan barang ke keranjang belanja
def add_item(cart, products):
    while True:
        kode_barang = input("Masukkan kode barang (atau 'selesai' untuk mengakhiri): ")
        if kode_barang.lower() == 'selesai':
            break

        if kode_barang in products:
            try:
                jumlah = int(input(f"Masukkan jumlah {products[kode_barang]['nama']}: "))
                if jumlah > 0:
                    cart.append({'kode': kode_barang, 'nama': products[kode_barang]['nama'], 'harga': products[kode_barang]['harga'], 'jumlah': jumlah})
                    print(f"{jumlah} {products[kode_barang]['nama']} ditambahkan ke keranjang.")
                else:
                    print("Jumlah harus lebih dari 0.")
            except ValueError:
                print("Masukkan jumlah yang valid (angka).")
        else:
            print("Kode barang tidak ditemukan.")

# Fungsi untuk melihat isi keranjang belanja
def view_cart(cart):
    if not cart:
        print("Keranjang belanja Anda kosong.")
        return

    print("\n=== Isi Keranjang Belanja ===")
    total_item = 0
    for item in cart:
        print(f"{item['nama']} ({item['jumlah']} x Rp{item['harga']:.2f})")
        total_item += item['jumlah']
    print(f"Total Item: {total_item}")

# Fungsi untuk menghapus barang dari keranjang
def remove_item(cart):
    if not cart:
        print("Keranjang belanja Anda kosong.")
        return

    view_cart(cart)
    try:
        index = int(input("Masukkan nomor barang yang ingin dihapus (mulai dari 1): ")) - 1
        if 0 <= index < len(cart):
            deleted_item = cart.pop(index) # Simpan barang yang dihapus
            print(f"{deleted_item['nama']} dihapus dari keranjang.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Masukkan nomor barang yang valid (angka).")

# Fungsi untuk menghitung total belanja
def calculate_total(cart):
    total = 0
    for item in cart:
        total += item['harga'] * item['jumlah']
    return total

# Fungsi untuk menyimpan transaksi ke dalam file
def save_transaction(cart, total):
    if not cart:
        print("Tidak ada transaksi untuk disimpan karena keranjang kosong.")
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"transaksi_{timestamp}.txt"
    try:
        with open(filename, "w") as file:
            file.write("=== Transaksi Pembelian ===\n")
            file.write(f"Waktu: {timestamp}\n")
            file.write("--- Barang ---\n")
            for item in cart:
                file.write(f"{item['nama']} ({item['jumlah']} x Rp{item['harga']:.2f})\n")
            file.write(f"Total: Rp{total:.2f}\n")
        print(f"Transaksi berhasil disimpan ke {filename}")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan transaksi: {e}")

# Fungsi untuk menampilkan riwayat transaksi dari file
def view_transaction_history():
    import os
    files = [f for f in os.listdir('.') if f.startswith('transaksi_') and f.endswith('.txt')] #List all files that start with transaksi_
    if not files:
        print("Belum ada riwayat transaksi.")
        return
    print("\n=== Riwayat Transaksi ===")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")
    while True:
        try:
            pilihan = input("Masukkan nomor transaksi yang ingin dilihat (atau '0' untuk kembali): ")
            if pilihan == '0':
                break
            pilihan = int(pilihan) - 1
            if 0 <= pilihan < len(files):
                with open(files[pilihan], "r") as file:
                    print(file.read())
            else:
                print("Nomor transaksi tidak valid")
        except ValueError:
            print("Masukkan nomor transaksi yang valid")

# Fungsi utama program
def main():
    # Daftar produk (bisa disimpan di database atau file eksternal)
    products = {
        'BRG001': {'nama': 'Laptop', 'harga': 8000000},
        'BRG002': {'nama': 'Mouse', 'harga': 100000},
        'BRG003': {'nama': 'Keyboard', 'harga': 250000},
        'BRG004': {'nama': 'Monitor', 'harga': 1500000},
        'BRG005': {'nama': 'Headset', 'harga': 500000},
    }
    cart = [] # Keranjang Belanja
    while True:
        display_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            add_item(cart, products)
        elif pilihan == '2':
            view_cart(cart)
        elif pilihan == '3':
            remove_item(cart)
        elif pilihan == '4':
            total = calculate_total(cart)
            print(f"Total belanja Anda: Rp{total:.2f}")
        elif pilihan == '5':
            total = calculate_total(cart)
            save_transaction(cart, total)
            cart = [] # Reset cart setelah menyimpan transaksi
        elif pilihan == '6':
            view_transaction_history()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan Aplikasi Kasir Mini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
