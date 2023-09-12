Link : https://medicine-stock-naomi.adaptable.app 

Cara saya mengimplementaikan seluruh checklist di atas adalah:
1. Saya membuat folder baru dengan nama Medicine_Stock pada lokal saya untuk menginisiasi repositori baru dan mengonfigurasi git pada folder ini. Saya juga membuat file README.md pada folder ini. Lalu saya membuat repository baru pada GitHub saya dengan visibilitas publik. Lalu saya membuat branch utama baru dan menghubungkan repository lokal saya dengan repository yang ada di GitHub saya kemudian melakukan push, sehingga file README saya sekarang sudah ada di repository GitHub saya. Setelah itu pada Git CMD saya, saya masuk ke direktori Medicine_Stock tadi lalu membuat dan menjalankan virtual environment. Lalu pada folder yang sama, saya membuat file requirements.txt yang berisi dependencies yang saya butuhkan untuk projek ini dan meng-install dependecies ini pada virtual environment. Lalu saya membuat projek django baru. Setelah itu, saya melihat bahwa ada kesalahan pada struktur file yang saya buat, sehingga saya membenarkannya dengan cara memastikan bahwa file README, requirements, manage, db.sqlite3 berada pada direktori utama, dan file init,asgi,settings,urls, dan wsgi pada direktori proyek. Lalu saya mengedit settings.py untuk mengizinkan semua host untuk bisa mengakses app. Lalu saya membuat berkas .gitignore pada direktori utama untuk mengabaikan berkas-berkas yang perlu diabaikan oleh Git. Setelah itu, saya melakukan add, commit, dan push untuk mengupdate repository GitHub saya agar sesuai dengan local saya setelah dilakukan perubahan. Lalu saya mendeploy app ini pada Adaptable

2. Setelah memastikan bahwa virtual environment masih aktif, pada direktori utama Medicine_Stock saya membuka aplikasi main dengan perintah python manage.py startapp main. Lalu saya mendaftarkan app main tadi dengan menambahkan 'main' pada variabel INSTALLED_APPS yang ada pada settings.py pada direktori proyek shopping_list.

3. Pada file urls.py yang ada pada direktori proyek, pada bagian urlpatterns kita tambahkan path('main/', include('main.urls')). Path ada fungsi yang digunakan untuk menyocokkan pola URL kemudian menjalankan fungsi views yang sesuai. Pada bagian ini, 'main/' adalah pola URL yang akan dicocokan sehingga jika pada URL ada 'main/' maka Django akan mencari file main.urls yang nantinya akan memetakan pola URL selanjutnya ke fungsi views yang sesuai.

4. Buka berkas models.py pada direktori main, di sini kita membuat model dengan nama Item. Melalui model ini kita mendefinisikan struktur basis data kita termasuk menentukan jenis dari masing-masing atribut yaitu name berupa CharField, amount berupa IntegerField dan description berupa TextField. Lalu saya melakukan migrasi model untuk melacak perubahan pada model basis data.

5. Kemudian saya membuka file views.py yang ada pada direktori main saya. Di sini, saya akan membuat function-function yang nantinya akan dipanggil jika pola URLnya sesuai. Pada project ini, saya membuat function show_main yang akan me-pass data name dan class ke template saat dirender. Di sini saya membuat context yaitu sebuah dictionary yang menyimpan data yang akan kita pass ke template karena kita belum menggunakan model dan data base.Saya membuat direktori baru bernama templates pada direktori main yang berisi berkas main.html. Berkasi ini berisi nama aplikasi dan juga template tag yang nantinya akan digantikan dengan value dari data yang dirender pada views.

6. Setelah Django melakukan pengecekan pada urls yang ada di direktori proyek, jika terdapat pola 'main/' maka Django akan mengecek file urls yang ada pada direktori main. Maka saya membuat file urls.py pada direktori main. Lalu saya mengimport path dari django.urls dan juga function views yang ingin digunakan. Lalu saya juga mendefine app_main untuk memberikan nama unik untuk app itu pada URL nantinya. Lalu saya menggunakan fungsi path pada variabel urlpatterns. Fungsi path ini menerima 3 argumen, yang pertama adalah pola URL yang akan dicocokan nantinya dalam hal ini polanya adalah '' (string kosong) sehingga maksudnya adalah home page dari app main itu sendiri, lalu fungsi pada views yang akan dipanggil jika pola URLnya sesuai (akan dipanggil fungsi show_main jika setelah /main adalah string kosong), kemudian name (ini opsional) supaya jika kita ingin merujuk pada URL ini pada bagian lain dari file ini, kita hanya perlu menyebut nama saja, tanpa perlu menuliskan URL lengkapnya.

7. Karena saya sudah melakukan deployment dari awal, saya hanya perlu melakukan add,commit, push direktori utama Medicine_Stock secara keseluruhan sehingga seluruh perubaha yang saya lakukan pada local akan tercatat pada direktori GitHub saya. Setelah itu Adaptable akan otomatis melakukan deployment ulang saat ada perubahan pada GitHub sourcenya.


Bagan request client ke web aplikasi berbasis Django beserta responnya:
![BAGAN](../bagan.png)
Jadi saat client mengirimkan request berupa sebuah URL, URL ini akan diterima dan dicek polanya oleh urls.py. Kemudian, jika ada pola yang sesuai dengan URL request, maka akan dikirimkan views yang sesuai. Lalu views akan menampilkan template yang sesuai dengan requestnya. Jika ternyata views butuh data dari database, maka dia akan sampaikan ke model untuk merequest data yang dibutuhkan. Lalu model akan membuat struktur data sesuai dengan request dan akan meminta data ke database, sehingga hanya data yang dibutuhkan saja yang kita ambil dari database. Kemudian data tersebut akan dikirimkan ke model, dan model akan mengirimkan data tersebut ke views, lalu views akan merender data tersebut ke html sehingga nantinya data tersebut akan muncul pada halaman web sesuai dengan template htmlnya. Lalu webpage akan dikembalikan dan ditampilkan kepada client.


Alasan kita menggunakan virtual environment adalah untuk mengisolasi projek kita dengan proyek lainnya sehingga setiap proyek memiliki environmentnya sendiri. Hal ini dapat menghindarkan kita dari konflik dependensi seandainya kita mengerjakan beberapa proyek yang berbeda secara bersamaan atau ketika proyek-proyek kita menggunakan versi Django atau versi python yang berbeda.

Memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun best practicenya adalah menggunakan virtual environment untuk menghindari masalah-masalah yang nantinya akan mungkin muncul dan juga untuk menjada lingkungan pengembangan python tetap tertatur, bersih, dan aman.

MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang menerapkan prinsip separation of concern. Prinsip ini memisahkan perangkat lunak menjadi beberapa komponen yang mana masing-masing komponen bertanggung jawab untuk suatu askpek dalam perangkat lunak. Perbedaan di antara ketiga arsitektur ini adalah cara mereka menerapkan separation of concern atau cara mereka memisahkan komponen pada perangkat lunaknya sehingga ada beberapa komponen yang berbeda.

MVC (Model-View-Controller):\n
    - Model = berhubungan dengan data
    - View: berhubungan dengan user interface dan menampilkan data
    - Controller : Mengontrol application flow dan user input
MVT (Model-View-Template):
    - Model = berhubungan dengan data
    - View: berhubungan dengan user interface dan menampilkan data
    - Template : Bertanggung jawab untuk HTML rendering (mengatur tampilan) dan menggabungkan data dari Model dan View ke dalam HTML.
MVVM (Model-View-ViewModel)
    - Model = berhubungan dengan data
    - View: berhubungan dengan user interface dan menampilkan data
    - ViewModel : Berperan sebagai perantara antara Model dan View. ViewModel bertanggung jawab untuk menyiapkan data untuk view dan memperbarui view saat data berubah.

Perbedaan utama dari ketiganya adalah pada komponen controller pada MVC, template pada MVT dan ViewModel pada MVVM