Link : https://medicine-stock-naomi.adaptable.app 

<h1> Tugas 2 </h1>

<h2>Cara saya mengimplementaikan seluruh checklist </h2>
1. Saya membuat folder baru dengan nama Medicine_Stock pada lokal saya untuk menginisiasi repositori baru dan mengonfigurasi git pada folder ini. Saya juga membuat file README.md pada folder ini. Lalu saya membuat repository baru pada GitHub saya dengan visibilitas publik. Lalu saya membuat branch utama baru dan menghubungkan repository lokal saya dengan repository yang ada di GitHub saya kemudian melakukan push, sehingga file README saya sekarang sudah ada di repository GitHub saya. Setelah itu pada Git CMD saya, saya masuk ke direktori Medicine_Stock tadi lalu membuat dan menjalankan virtual environment. Lalu pada folder yang sama, saya membuat file requirements.txt yang berisi dependencies yang saya butuhkan untuk projek ini dan meng-install dependecies ini pada virtual environment. Lalu saya membuat projek django baru. Setelah itu, saya melihat bahwa ada kesalahan pada struktur file yang saya buat, sehingga saya membenarkannya dengan cara memastikan bahwa file README, requirements, manage, db.sqlite3 berada pada direktori utama, dan file init,asgi,settings,urls, dan wsgi pada direktori proyek. Lalu saya mengedit settings.py untuk mengizinkan semua host untuk bisa mengakses app. Lalu saya membuat berkas .gitignore pada direktori utama untuk mengabaikan berkas-berkas yang perlu diabaikan oleh Git. Setelah itu, saya melakukan add, commit, dan push untuk mengupdate repository GitHub saya agar sesuai dengan local saya setelah dilakukan perubahan. Lalu saya mendeploy app ini pada Adaptable

2. Setelah memastikan bahwa virtual environment masih aktif, pada direktori utama Medicine_Stock saya membuka aplikasi main dengan perintah python manage.py startapp main. Lalu saya mendaftarkan app main tadi dengan menambahkan 'main' pada variabel INSTALLED_APPS yang ada pada settings.py pada direktori proyek shopping_list.

3. Pada file urls.py yang ada pada direktori proyek, pada bagian urlpatterns kita tambahkan path('main/', include('main.urls')). Path ada fungsi yang digunakan untuk menyocokkan pola URL kemudian menjalankan fungsi views yang sesuai. Pada bagian ini, 'main/' adalah pola URL yang akan dicocokan sehingga jika pada URL ada 'main/' maka Django akan mencari file main.urls yang nantinya akan memetakan pola URL selanjutnya ke fungsi views yang sesuai.

4. Buka berkas models.py pada direktori main, di sini kita membuat model dengan nama Item. Melalui model ini kita mendefinisikan struktur basis data kita termasuk menentukan jenis dari masing-masing atribut yaitu name berupa CharField, amount berupa IntegerField dan description berupa TextField. Lalu saya melakukan migrasi model untuk melacak perubahan pada model basis data.

5. Kemudian saya membuka file views.py yang ada pada direktori main saya. Di sini, saya akan membuat function-function yang nantinya akan dipanggil jika pola URLnya sesuai. Pada project ini, saya membuat function show_main yang akan me-pass data name dan class ke template saat dirender. Di sini saya membuat context yaitu sebuah dictionary yang menyimpan data yang akan kita pass ke template karena kita belum menggunakan model dan data base.Saya membuat direktori baru bernama templates pada direktori main yang berisi berkas main.html. Berkasi ini berisi nama aplikasi dan juga template tag yang nantinya akan digantikan dengan value dari data yang dirender pada views.

6. Setelah Django melakukan pengecekan pada urls yang ada di direktori proyek, jika terdapat pola 'main/' maka Django akan mengecek file urls yang ada pada direktori main. Maka saya membuat file urls.py pada direktori main. Lalu saya mengimport path dari django.urls dan juga function views yang ingin digunakan. Lalu saya juga mendefine app_main untuk memberikan nama unik untuk app itu pada URL nantinya. Lalu saya menggunakan fungsi path pada variabel urlpatterns. Fungsi path ini menerima 3 argumen, yang pertama adalah pola URL yang akan dicocokan nantinya dalam hal ini polanya adalah '' (string kosong) sehingga maksudnya adalah home page dari app main itu sendiri, lalu fungsi pada views yang akan dipanggil jika pola URLnya sesuai (akan dipanggil fungsi show_main jika setelah /main adalah string kosong), kemudian name (ini opsional) supaya jika kita ingin merujuk pada URL ini pada bagian lain dari file ini, kita hanya perlu menyebut nama saja, tanpa perlu menuliskan URL lengkapnya.

7. Karena saya sudah melakukan deployment dari awal, saya hanya perlu melakukan add,commit, push direktori utama Medicine_Stock secara keseluruhan sehingga seluruh perubaha yang saya lakukan pada local akan tercatat pada direktori GitHub saya. Setelah itu Adaptable akan otomatis melakukan deployment ulang saat ada perubahan pada GitHub sourcenya.


<h2>Bagan request client ke web aplikasi berbasis Django beserta responnya </h2>

![BAGAN](./bagan.png)
Jadi saat client mengirimkan request berupa sebuah URL, URL ini akan diterima dan dicek polanya oleh urls.py. Kemudian, jika ada pola yang sesuai dengan URL request, maka akan dikirimkan views yang sesuai. Lalu views akan menampilkan template yang sesuai dengan requestnya. Jika ternyata views butuh data dari database, maka dia akan sampaikan ke model untuk merequest data yang dibutuhkan. Lalu model akan membuat struktur data sesuai dengan request dan akan meminta data ke database, sehingga hanya data yang dibutuhkan saja yang kita ambil dari database. Kemudian data tersebut akan dikirimkan ke model, dan model akan mengirimkan data tersebut ke views, lalu views akan merender data tersebut ke html sehingga nantinya data tersebut akan muncul pada halaman web sesuai dengan template htmlnya. Lalu webpage akan dikembalikan dan ditampilkan kepada client.

<h2> Alasan menggunakan virtual environment </h2>
Alasan kita menggunakan virtual environment adalah untuk mengisolasi projek kita dengan proyek lainnya sehingga setiap proyek memiliki environmentnya sendiri. Hal ini dapat menghindarkan kita dari konflik dependensi seandainya kita mengerjakan beberapa proyek yang berbeda secara bersamaan atau ketika proyek-proyek kita menggunakan versi Django atau versi python yang berbeda.

Memungkinkan untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun best practicenya adalah menggunakan virtual environment untuk menghindari masalah-masalah yang nantinya akan mungkin muncul dan juga untuk menjada lingkungan pengembangan python tetap tertatur, bersih, dan aman.

<h2> MVC, MVT, dan MVVM </h2>
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang menerapkan prinsip separation of concern. Prinsip ini memisahkan perangkat lunak menjadi beberapa komponen yang mana masing-masing komponen bertanggung jawab untuk suatu askpek dalam perangkat lunak. Perbedaan di antara ketiga arsitektur ini adalah cara mereka menerapkan separation of concern atau cara mereka memisahkan komponen pada perangkat lunaknya sehingga ada beberapa komponen yang berbeda.

MVC (Model-View-Controller):<br>
    - Model = berhubungan dengan data <br>
    - View: berhubungan dengan user interface dan menampilkan data <br>
    - Controller : Mengontrol application flow dan user input <br>
MVT (Model-View-Template): <br>
    - Model = berhubungan dengan data <br>
    - View: berhubungan dengan user interface dan menampilkan data <br>
    - Template : Bertanggung jawab untuk HTML rendering (mengatur tampilan) dan menggabungkan data dari Model dan View ke dalam HTML <br>
MVVM (Model-View-ViewModel)
    - Model = berhubungan dengan data <br>
    - View: berhubungan dengan user interface dan menampilkan data <br>
    - ViewModel : Berperan sebagai perantara antara Model dan View. ViewModel bertanggung jawab untuk menyiapkan data untuk view dan memperbarui view saat data berubah. <br>

Perbedaan utama dari ketiganya adalah pada komponen controller pada MVC, template pada MVT dan ViewModel pada MVVM

<h1> Tugas 2 </h1>

<h2> Perbedaan antara form POST dan GET dala, Django </h2> 
1. Metode Pengiriman Data dan Keamanan <br>
* POST : Data dikirimkan sebagai bagian dari body permintaan HTTP tidak terlihat dalam URL <br>
* GET : Data dikirimkan sebagai parameter di URL <br>

2. Penggunaan
* POST : Digunakan ketika ingin mengirimkan data yang akan memengaruhi perubahan di server
* GET : Digunakan ketika ingin mengambil data dari server 

3. Keamanan
* POST : Lebih aman karena data tidak terlihat dalam URL
* GET : Kurang aman karena data dapat dilihat pada URL 

4. Penangan Data:
* POST : Ditangani oleh view Django yang menggunakan metode request.POST atau request.FILES (jika ada unggahan file)
* GET : Ditangani oleh view Django yang menggunakan metode request.GET 

<h2>  Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data </h2>
1. XML : Menggunakan tag pembuka dan penutup untuk mengelilingi data (mirip seperti HTML). Setiap elemen atau node memiliki struktur hierarki yang jelas. Struktur ini berbentuk seperti struktur pohon yang dimulai dengan elemen akar/induk baru kemudian elemen anak. <br>
2. JSON : Menggunakan pasangan key dan values dalam tanda kurung kurawal sehingga lebih mudah dibaca oleh manusia. <br>
3. HTML : tidak secara khusus dirancang untuk pengiriman data. Namun, bisa digunakan untuk mengirimkan data dalam bentuk formulir. HTML lebih sering digunakan untuk membuat struktur halaman web. <br>

<h2> Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern </h2>
1. Memiliki sintaks yang sederhana dan mudah dibaca oleh manusia <br>
2. JSON memiliki overhead yang rendah dalam hal ukuran data sehingga lebih ringan dan cepat dalam pengiriman data <br>
3. JSON bisa dipahami oleh hampir semua bahasa pemrograman <br>
4. JSON mendukung berbagai tipe data (termasuk array) sehingga dapat menggambarkaan data yang kompleks dan dinamis dengan mudah.

<h2> Cara saya mengimplementasikan seluruh checklist</h2>

<h4> Membuat input form </h4>

Pertama saya membuat berkas form.py yang digunakan untuk membuat sebuah form dengan menggunakan kelas ModelForm berdasarkan model Item. Disini saya membuat kelas ProductForm yang mewarisi semua fitur dan fungsi dari kelas ModelForm. Lalu saya membuat kelas Meta yang di dalamnya memuat model yang akan menjadi dasar pembuatan form, dan juga menentukan bidang-bidang dari model Item yang akan dimasukkan dalam form ini.

Lalu saya membuat fungsi create_product pada file views.py yang ada di folder main yang menerima parameter request. Lalu saya membuat instance dari ProductForm. request.POST digunakan untuk mengisi form yang dikirimkan oleh pengguna dengan metode POST dan none untuk membuat form kosong ketika halaman pertama kali diakses.

Lalu saya membuat kondisi bahwa form hanya akan diproses jika data yang dikirimkan valid sesuai dengan yang didefinisikan pada ProductForm dan requestnya adalah POST. Setelah data berhasil disimpan, pengguna akan dibawa kembali ke home page. Jika requestnya adalah GET atau form tidak valid, maka akan merender form ini ke halaman create_product.html. Halaman ini berisi form yang memungkinkan pengguna untuk mengisi form.

Lalu ditambahkan url untuk memanggil fungsi create_product.

<h4> Membuat 5 fungsi </h4>
HTML : disini saya mengedit fungsi show_main sehingga merender juga seluruh item yang sudah disimpan di database. Kemudian pada main.html, saya tampilkan seluruh atribut dari item-item yang sudah dibuat tadi. <br>

XML : disini saya membuat fungsi show_xml yang mengambil seluruh data item yang sudah disimpan dalam database, kemudian menserialize menjadi format xml, lalu dikembalikan HttpResponse dengan content_type yang mengindikasikan bahwa response berisi data dalam format XML

JSON : disini saya membuat fungsi show_json yang mengambil seluruh data item yang sudah disimpan dalam database, kemudian menserialize menjadi format JSON, lalu dikembalikan HttpResponse dengan content_type yang mengindikasikan bahwa response berisi data dalam format JSON.

XML by ID : disini saya membuat fungsi show_xml_by_id yang menerima parameter request dan id. Fungsi ini engambil satu item berdasarkan ID yang ditentukan, kemudian menserialize menjadi format xml, lalu dikembalikan HttpResponse dengan content_type yang mengindikasikan bahwa response berisi data dalam format XML

JSON by ID : disini saya membuat fungsi show_json_by_id yang menerima parameter request dan id. Fungsi ini engambil satu item berdasarkan ID yang ditentukan, kemudian menserialize menjadi format JSON, lalu dikembalikan HttpResponse dengan content_type yang mengindikasikan bahwa response berisi data dalam format JSON

Lalu saya membuat URL routing untuk masing-masing fungsi view pada urls.py pada main folder

<h2> Screenshoot </h2>
HTML :

![show_main](./shown_main.png)
XML :

![XML](./xml.png)
JSON:

![JSON](./json.png)
XML by ID :

![XML_ID](./xml_id.png)
JSON by ID :

![JSON_ID](./json_id.png)








