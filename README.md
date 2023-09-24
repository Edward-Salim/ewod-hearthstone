<h1>README Tugas 4</h1>

1. **Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?**
    
    **Jawaban:**

    Django UserCreationForm adalah salah satu dari banyak formulir bawaan yang disediakan oleh Django. Formulir ini dirancang khusus untuk mempermudah proses pembuatan pengguna (user) dalam aplikasi web yang menggunakan Django. UserCreationForm memungkinkan pengembang untuk membuat formulir pendaftaran pengguna dengan cepat dan mudah tanpa perlu menulis kode dari awal.

    * **Kelebihan:**
        * **Mudah digunakan:**

            UserCreationForm telah disediakan oleh Django dengan semua logika yang diperlukan untuk membuat pengguna baru. Pengembang hanya perlu mengimpor formulir ini dan menggunakannya dalam tampilan mereka tanpa perlu menulis kode validasi pendaftaran dari awal.

        * **Keamanan Terintegrasi:**

            Formulir ini mencakup validasi bawaan untuk memastikan bahwa pengguna memberikan informasi yang benar saat mendaftar, seperti memeriksa apakah alamat email sudah digunakan atau belum.

        * **Kustomisasi:**

            Meskipun UserCreationForm adalah formulir bawaan, pengguna masih dapat mengkustomisasinya sesuai kebutuhan. Pengguna dapat menambahkan atau menghapus bidang tambahan, menyesuaikan pesan kesalahan, dan memodifikasi tampilan sesuai dengan desain aplikasi pengguna.

        * **Integrasi dengan Django's Authentication System:**

            UserCreationForm terintegrasi dengan baik dengan sistem otentikasi bawaan Django, yang berarti setelah pengguna berhasil mendaftar, mereka dapat langsung masuk ke aplikasi dengan menggunakan kredensial yang mereka buat.

    * **Kekurangan:**
        * **Terbatas pada Kebutuhan Khusus:**

            Jika aplikasi pengguna memiliki kebutuhan pendaftaran yang sangat khusus, pengguna mungkin perlu menulis formulir pendaftaran kustom dari awal daripada mengandalkan UserCreationForm.

        * **Tampilan Default Mungkin Tidak Sesuai:**

            Tampilan default UserCreationForm mungkin tidak sesuai dengan desain visual aplikasi pengguna. Oleh karena itu, pengguna perlu menghabiskan waktu untuk menyesuaikannya agar sesuai dengan gaya desainnya.

        * **Perlu Pemahaman Tentang Django:**

            Pengembang harus memahami bagaimana Django bekerja, termasuk konsep otentikasi dan manajemen pengguna, agar dapat menggunakan UserCreationForm dengan efektif.<br><br><br>


2. **Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?**

    **Jawaban:**

    * **Autentikasi:**
        * Autentikasi adalah proses verifikasi identitas pengguna. Ini adalah tahap di mana sistem memeriksa apakah pengguna yang mencoba mengakses aplikasi adalah orang yang mereka klaim dengan menggunakan kredensial tertentu, seperti nama pengguna dan kata sandi.
        * Di Django, autentikasi dapat diimplementasikan dengan menggunakan sistem otentikasi bawaan yang telah disediakan oleh Django. Sistem ini mengelola pengguna, sesi, dan otentikasi berbasis token.
    * **Otorisasi:**
        * Otorisasi adalah proses mengontrol akses pengguna yang telah diotentikasi ke berbagai bagian dari aplikasi atau sumber daya tertentu. Ini adalah tahap di mana aplikasi menentukan apa yang diizinkan atau dilarang oleh pengguna yang masuk, berdasarkan peran atau izin yang mereka miliki.
        * Di Django, otorisasi dapat diimplementasikan dengan menggunakan sistem otentikasi bawaan yang disertai dengan sistem izin. Sistem izin Django memungkinkan pengguna untuk menentukan siapa yang dapat melakukan operasi apa pada model-data dalam aplikasi.

    Autentikasi dan otorisasi memiliki peran yang sangat penting dalam ekosistem keamanan aplikasi web. Dalam konteks Django, bersama-sama, autentikasi dan otorisasi membentuk pondasi yang kokoh untuk menjaga aplikasi dari potensi ancaman dan risiko keamanan. Autentikasi bertanggung jawab untuk memverifikasi identitas pengguna, memastikan bahwa hanya individu yang sah yang memiliki hak akses ke dalam sistem. Di sisi lain, otorisasi memastikan bahwa setiap pengguna yang telah diotentikasi memiliki izin yang sesuai untuk melakukan tindakan tertentu dalam aplikasi, sehingga mencegah penggunaan yang tidak sah atau penyalahgunaan hak akses.<br><br><br>

3. **Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**

    **Jawaban:**


    Cookies adalah mekanisme kecil yang digunakan dalam pengembangan aplikasi web untuk menyimpan data pada sisi klien (browser pengguna). Cookies adalah file kecil berisi informasi teks yang dikirim oleh server web ke browser pengguna dan disimpan di sana. Informasi ini kemudian dapat diakses oleh server web saat pengguna melakukan permintaan berikutnya, sehingga memungkinkan server untuk menyimpan dan mengambil data di antara kunjungan pengguna ke situs web. Django menyediakan dukungan bawaan untuk mengelola cookies dan sesi pengguna.


    Berikut adalah langkah umum yang terjadi ketika Django menggunakan cookies untuk mengelola sesi pengguna:

    1. Ketika pengguna pertama kali mengakses aplikasi web Django, server akan membuat cookie sesi baru yang berisi identifier unik untuk sesi pengguna.
    2. Identifier sesi ini akan disimpan di cookie di sisi klien pengguna.
    3. Setiap permintaan berikutnya dari pengguna akan mencakup cookie sesi ini, yang memungkinkan server untuk mengidentifikasi pengguna yang sesuai dengan sesi tertentu.
    4. Django dapat menyimpan data sesi pengguna, seperti informasi login atau preferensi, di server, dan mengaitkannya dengan sesi yang sesuai melalui identifier yang ada di cookie.
    5. Data sesi ini dapat diakses dan dimodifikasi oleh server untuk menjaga keadaan sesi pengguna selama interaksi mereka dengan aplikasi.<br><br><br>
4. **Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?**

    **Jawaban:**


    Penggunaan cookies dalam pengembangan web dapat aman jika dilakukan dengan benar dan dengan mempertimbangkan beberapa risiko potensial yang terkait dengan cookies. Berikut adalah beberapa pertimbangan terkait dengan keamanan penggunaan cookies:

    * **Privasi Pengguna:**

        Pengguna memiliki hak privasi, dan penggunaan cookies yang berlebihan atau melacak informasi pribadi pengguna tanpa izin dapat melanggar privasi pengguna. Pastikan untuk mematuhi regulasi privasi seperti GDPR (General Data Protection Regulation) dan memberikan pengguna opsi kontrol terhadap cookies, seperti pengaturan untuk menolak cookies.

    * **Risiko Pencurian Informasi:**

        Cookies dapat mengandung data sensitif, seperti token otentikasi atau informasi sesi pengguna. Jika cookies ini tidak dienkripsi atau tidak diatur dengan benar, ada risiko pencurian informasi oleh pihak yang tidak berwenang.

    * **Risiko Cross-Site Scripting (XSS):**

        Cookies yang tidak aman dapat menjadi sumber masalah XSS jika data dari cookies disisipkan dalam halaman web tanpa sanitasi yang memadai. Penyerang dapat mencoba menyisipkan skrip berbahaya dalam cookies untuk mengakses atau mencuri data pengguna lainnya.

    * **Risiko CSRF (Cross-Site Request Forgery):**

        Cookies dapat digunakan untuk menyimpan token anti-CSRF yang digunakan untuk melindungi terhadap serangan CSRF. Namun, jika tidak diatur dengan benar, cookies ini dapat dicuri oleh serangan pencurian cookies (cookie theft), yang mengakibatkan risiko CSRF.

    * **Risiko Keamanan dari Cookie Jar:**

        Penggunaan cookies yang tidak diatur dengan benar dapat mengakibatkan risiko keamanan bagi pengguna, seperti penyerangan session hijacking atau session fixation. Oleh karena itu, pastikan untuk menjalankan praktik terbaik dalam manajemen cookies, seperti mengeluarkan cookies saat pengguna logout atau mengganti session ID secara berkala.<br><br><br>

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.**

    **Jawaban:**

    1. **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**

        1. Saya akan membuat halaman utama (main) menjadi terbatas dengan mengharuskan pengguna untuk membuat akun dan login. Untuk membuat formulir pendaftaran pengguna, saya memanfaatkan Django's UserCreationForm, yang memudahkan pembuatan formulir pendaftaran.
        2. Pertama, saya membuat fungsi register di dalam file views.py yang terletak di subdirektori main. Fungsi ini bertujuan untuk secara otomatis menghasilkan formulir pendaftaran dan membuat akun pengguna ketika data dari formulir tersebut di-submit. Saat pengguna mengirimkan data pendaftaran melalui formulir, saya membuat instance UserCreationForm baru dengan menggunakan data yang diterima dari request.POST. Kemudian, saya memeriksa apakah data yang dimasukkan oleh pengguna valid dengan menggunakan metode form.is_valid(). Jika formulir valid, saya menggunakan metode form.save() untuk membuat dan menyimpan data pengguna ke dalam basis data. Saya juga menampilkan pesan sukses kepada pengguna dengan menggunakan messages.success(request, 'Akun Anda telah berhasil dibuat!'). Terakhir, saya menggunakan return redirect('main:show_main') untuk mengarahkan pengguna ke halaman utama (show_main) setelah data formulir berhasil disimpan. Dengan demikian, pengguna akan masuk ke dalam aplikasi setelah mendaftar. Saya juga membuat berkas HTML baru dengan nama register.html di dalam folder main/templates, dan kemudian mengisi berkas tersebut dengan kode HTML yang diperlukan untuk menampilkan halaman pendaftaran dengan baik.
        3. Kemudian, saya kembali ke berkas views.py dan mengimpor fungsi authenticate dan login dari modul yang sesuai. Selanjutnya, saya membuat sebuah fungsi bernama login yang bertujuan untuk mengimplementasikan mekanisme autentikasi pengguna saat mereka mencoba untuk masuk ke dalam aplikasi. Dalam fungsi ini, saya menggunakan authenticate(request, username=username, password=password) untuk melakukan autentikasi pengguna berdasarkan username dan password yang diterima dari permintaan (request) yang dikirim oleh pengguna saat melakukan proses login. Selain itu, saya juga menciptakan berkas login.html dalam folder main/templates untuk menampilkan halaman login dengan antarmuka pengguna yang sesuai.
        4. Kemudian, saya kembali ke berkas views.py dan mengimpor fungsi logout untuk mengimplementasikan mekanisme logout dalam aplikasi. Saya membuat sebuah fungsi bernama logout, yang digunakan untuk mengatur proses logout. Dalam fungsi ini, saya menggunakan logout(request) untuk menghapus sesi pengguna yang saat ini masuk. Ini berarti bahwa pengguna akan keluar dari sesi mereka dan tidak lagi dianggap sebagai pengguna yang terautentikasi. Setelah melakukan logout, saya menggunakan return redirect('main:login') untuk mengarahkan pengguna kembali ke halaman login dalam aplikasi Django. Selanjutnya, saya juga menambahkan tombol logout pada berkas main.html.
        5. Selanjutnya, saya mengimpor semua fungsi yang telah saya buat sebelumnya ke berkas urls.py yang terletak di dalam subdirektori main. Setelah itu, saya menambahkan path URL ke dalam variabel urlpatterns untuk mengatur cara akses ke semua fungsi yang sudah diimpor sebelumnya. Pathnya yaitu path('register/', register, name='register'), path('login/', login_user, name='login'), dan path('logout/', logout_user, name='logout').
        6. Kemudian, saya melanjutkan dengan mengimplementasikan pembatasan akses ke halaman utama (main) dalam aplikasi. Untuk melakukan ini, pertama-tama saya mengimpor login_required ke dalam berkas views.py yang berada di dalam subdirektori main. Kemudian, saya menambahkan dekorator @login_required(login_url='/login') di atas fungsi show_main yang bertujuan untuk membatasi akses ke halaman utama. Dengan penambahan kode tersebut, saya memastikan bahwa hanya pengguna yang sudah login (terautentikasi) yang dapat mengakses halaman utama.

    2. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**

        1. Pertama, saya menjalankan proyek Django dengan menjalankan perintah python manage.py runserver dan kemudian membuka alamat http://localhost:8000/ di browser. Setelah halaman utama aplikasi terbuka, saya melanjutkan dengan melakukan beberapa tindakan. Saya mengklik hyperlink "Register Now" untuk mendaftar dan membuat dua akun pengguna. Akun pertama saya beri nama pengguna "Ikan" dengan kata sandi "1234567%", dan akun kedua saya beri nama pengguna "Bungres" dengan kata sandi "0000000!". Setelah berhasil membuat kedua akun tersebut, saya melakukan login ke akun pertama ("Ikan"). Setelah login, saya memiliki akses ke aplikasi dan dapat melanjutkan dengan menambahkan tiga data kartu. Saya menggunakan tombol "Add New Item" untuk menambahkan data kartu tersebut. Sama halnya, saya melakukan tindakan yang sama pada akun kedua ("Bungres") dengan menambahkan tiga data kartu lainnya. Terakhir, setelah selesai menggunakan aplikasi, saya melakukan logout dengan mengklik tombol "Logout". Tindakan ini mengakhiri sesi saya dan mengarahkan saya kembali ke halaman login.

    3. **Menghubungkan model Item dengan User.**

        1. Sekarang, saya ingin menghubungkan setiap objek "Item" yang akan dibuat dengan pengguna yang membuatnya. Hal ini akan memastikan bahwa pengguna yang telah diautentikasi hanya dapat melihat dan mengelola item yang telah mereka buat sendiri.
        2. Pertama, saya mengimpor model "User" dari django.contrib.auth.models ke dalam berkas views.py yang berada di dalam subdirektori main. Hal ini diperlukan untuk mengakses informasi pengguna terkait. Selanjutnya, saya memperbarui model "Item" yang sudah ada dengan menambahkan potongan kode user = models.ForeignKey(User, on_delete=models.CASCADE). Potongan kode ini menghubungkan setiap objek "Item" dengan satu objek "User" melalui sebuah relasi. Ini berarti bahwa setiap item akan terkait dengan satu pengguna (user), dan setiap item akan memiliki informasi tentang siapa yang membuatnya. Kemudian, saya melakukan perubahan pada fungsi create_item. Di dalamnya, saya menggunakan kode item = form.save(commit=False), item.user = request.user, dan item.save(). Parameter commit=False digunakan untuk mencegah Django dari menyimpan objek yang telah dibuat dari formulir secara langsung ke basis data. Hal ini memberi kesempatan untuk memodifikasi objek tersebut sebelum menyimpannya. Dalam kasus ini, saya ingin mengisi field "user" dengan objek "User" yang sesuai dengan pengguna yang sedang login untuk menandakan bahwa objek "Item" tersebut dimiliki oleh pengguna yang saat ini diautentikasi.
        3. Setelah melakukan semua perubahan ini, saya menyimpan semua perubahan yang telah dilakukan. Namun, saat melakukan migrasi model dengan perintah python manage.py makemigrations, saya mengalami masalah dan muncul pesan error. Untuk menyelesaikan masalah tersebut, saya memilih untuk menetapkan nilai default untuk field "user" pada semua baris yang telah ada dalam basis data. Saya mengetikkan angka 1 untuk menetapkan user dengan ID 1 (yang telah dibuat sebelumnya) sebagai nilai default. Ini memungkinkan saya untuk menyelesaikan migrasi model tanpa kesalahan. Kemudian, saya menjalankan perintah python manage.py migrate untuk mengaplikasikan migrasi tersebut ke dalam basis data.

    4. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**

        1. Pertama, saya melakukan perubahan pada fungsi show_main yang ada pada views.py di subdirektori main untuk memastikan bahwa hanya objek "Item" yang terasosiasi dengan pengguna yang saat ini login yang akan ditampilkan. Ini dilakukan dengan menyaring semua objek "Item" dan hanya mengambil item yang memiliki field "user" yang sesuai dengan pengguna yang sedang login. Selanjutnya, saya mengubah value ‘nama’ pada context dengan ‘nama’: request.user.username untuk menampilkan username pengguna yang saat ini login pada halaman utama agar pengguna dapat melihat dengan jelas akun yang mereka gunakan.
        2. Kemudian, saya menambahkan perintah import datetime pada bagian paling atas berkas kode. Dalam fungsi login_user, saya menambahkan beberapa kode tambahan untuk mengelola informasi cookie yang disebut last_login, yang akan digunakan untuk melihat kapan terakhir kali pengguna melakukan login. Saya menggunakan login(request, user) untuk melakukan proses login pengguna terlebih dahulu. Kemudian, saya membuat objek response dengan perintah response = HttpResponseRedirect(reverse("main:show_main")). Ini digunakan untuk membuat respons yang akan diarahkan ke halaman utama setelah login berhasil. Selanjutnya, saya menambahkan perintah response.set_cookie('last_login', str(datetime.datetime.now())) untuk membuat cookie last_login dan menambahkannya ke dalam respons. Cookie ini akan berisi informasi waktu saat pengguna terakhir kali melakukan login. Dalam fungsi show_main, saya memperbarui variabel konteks dengan menambahkan potongan kode 'last_login': request.COOKIES['last_login']. Hal ini bertujuan untuk memasukkan informasi dari cookie last_login ke dalam variabel konteks. Terakhir, dalam fungsi logout_user, saya menambahkan perintah response.delete_cookie('last_login') untuk menghapus cookie last_login saat pengguna melakukan logout.
        3. Saya juga menambahkan elemen HTML &lt;h5>Sesi terakhir login: {{ last_login }}&lt;/h5> ke dalam berkas main.html. Ini akan menampilkan informasi tentang sesi terakhir login pengguna pada halaman utama.