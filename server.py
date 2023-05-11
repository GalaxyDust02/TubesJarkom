import socket  # Impor modul socket

server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)  # Buat objek server socket
# Ikatan server socket ke localhost dan port 8080
server_socket.bind(('localhost', 1414))
server_socket.listen(1)  # Dengarkan koneksi masuk
# Cetak pesan yang menunjukkan bahwa server sedang mendengarkan di port 8080
print(f'Server sedang mendengarkan di port 1414')
while True:  # Mulai loop tak terbatas
    client_socket, client_address = server_socket.accept()  # Terima koneksi masuk
    # Terima data dari klien dan decode itu
    request = client_socket.recv(1024).decode()
    if request:  # Jika ada permintaan
        request_parts = request.split()  # Pisahkan permintaan menjadi bagian-bagian
        if len(request_parts) > 1:  # Jika ada lebih dari satu bagian dalam permintaan
            # Dapatkan nama file dari bagian kedua permintaan
            filename = request_parts[1]
            try:  # Coba buka file
                with open(filename[1:], 'rb') as file:  # Buka file dalam mode biner
                    response = file.read()  # Baca isi file

                # Buat header HTTP dengan status 200 OK dan jenis konten file
                header = f'HTTP/1.1 200 OK\nContent-Type:\n\n'
                # Cetak pesan yang menunjukkan bahwa file ditemukan dan dikirim dengan sukses
                print(f'{filename} - OK')
            except:  # Jika terjadi kesalahan saat mencoba membuka file
                # Buat header HTTP dengan status 404 Not Found
                header = 'HTTP/1.1 404 Not Found\n\n'
                response = b'404 Not Found'  # Tetapkan respons ke pesan 404 Not Found
                # Cetak pesan yang menunjukkan bahwa file tidak ditemukan
                print(f'{filename} - Not Found')
            # Kirim header HTTP dan respons ke klien
            client_socket.send(header.encode() + response)
    client_socket.close()
