**<h1>README Tugas 5</h1>**

1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

    **Jawaban:**

    Element selector adalah salah satu jenis selektor CSS yang digunakan untuk memilih elemen HTML berdasarkan tipe elemennya. Setiap elemen HTML memiliki tipe tertentu (misalnya, &lt;p>, &lt;div>, &lt;h1>, &lt;a>, dll.), dan elemen selector memungkinkan untuk memilih semua elemen dengan tipe tertentu tersebut.

    * **Universal Selector (*):**

        Selector ini memilih semua elemen di halaman web. Universal selector sebaiknya digunakan dengan hati-hati karena dapat mempengaruhi semua elemen pada halaman web. Penggunaannya yang berlebihan dapat mengakibatkan kinerja lambat. Biasanya, hanya digunakan jika diperlukan untuk reset styling secara umum atau beberapa keperluan khusus.

    * **Type Selector (Element Selector):**

        Selector ini memilih semua elemen dengan tipe yang sesuai. Type selector sangat berguna ketika ingin menerapkan styling atau aturan CSS secara khusus pada jenis elemen tertentu. Misalnya, jika ingin mengubah tampilan semua elemen &lt;p> pada halaman, dapat menggunakan selector p.  Begitu juga, selector ini umumnya digunakan pada berbagai jenis elemen seperti &lt;div>, &lt;a>, &lt;img>, &lt;ul>, &lt;ol>, &lt;li>, &lt;span>, &lt;table>, &lt;form>, &lt;section>, &lt;button>, &lt;textarea>, &lt;article>, &lt;aside>, &lt;header>, &lt;footer>, &lt;nav>, &lt;main>, &lt;h1> hingga &lt;h6>, dan banyak lagi.<br><br>

2. Jelaskan HTML5 Tag yang kamu ketahui.

    **Jawaban:**

    * **&lt;header>:** Digunakan untuk mendefinisikan bagian atas halaman atau bagian kepala dari sebuah elemen HTML. Ini sering digunakan untuk judul halaman, logo, dan elemen lainnya yang berkaitan dengan bagian atas halaman.

    * **&lt;nav>:** Digunakan untuk menentukan bagian navigasi dalam dokumen. Ini biasanya berisi tautan menu yang membantu pengguna berpindah antara halaman-halaman dalam situs web.

    * **&lt;main>:** Menunjukkan konten utama dari sebuah halaman web. Hanya boleh ada satu elemen &lt;main> dalam satu halaman.

    * **&lt;section>:** Digunakan untuk mengelompokkan konten yang terkait secara tematis dalam sebuah halaman. Ini membantu dalam pengorganisasian dan pemahaman struktur halaman.

    * **&lt;footer>:** Menunjukkan bagian bawah dari sebuah halaman atau bagian penutup. Ini sering digunakan untuk informasi kontak, tautan ke halaman lain, atau hak cipta.<br><br>

3. Jelaskan perbedaan antara margin dan padding.

    **Jawaban:**

    * **Margin:**

        Margin adalah ruang kosong di sekitar elemen HTML yang berfungsi sebagai jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya. Margin memengaruhi jarak antara elemen dengan elemen-elemen luar. Margin elemen akan mendorong elemen tersebut menjauh dari elemen lain di luar elemen tersebut. Margin bisa diterapkan pada semua elemen HTML dan digunakan untuk mengatur jarak antara elemen tersebut dengan elemen-elemen lain di luarnya.

    * **Padding:**

        Padding adalah ruang kosong di sekitar konten dalam elemen HTML. Ini berfungsi sebagai jarak antara konten elemen dan batas elemen itu sendiri. Padding memengaruhi jarak antara konten elemen dengan batas elemen. Ini tidak mempengaruhi jarak antara elemen tersebut dengan elemen luar. Padding biasanya diterapkan pada elemen-elemen yang memiliki konten, seperti &lt;div>, &lt;p>, atau elemen lain yang mengandung teks atau elemen lain di dalamnya.<br><br>

4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

    **Jawaban:**

    * **Bootstrap:**
        * Memiliki desain yang sudah ditetapkan dengan baik dan banyak komponen pra-didesain. Tampilan dan perilaku komponen seringkali sudah memiliki pola desain yang konsisten.

        * Bootstrap menggunakan banyak kelas CSS yang telah ditetapkan sebelumnya untuk mengaplikasikan gaya dan tampilan komponen. Hal ini dapat membuat kode HTML terlihat lebih bersih, tetapi juga memerlukan lebih banyak kelas dalam markup HTML.

        * Bootstrap cenderung lebih besar dalam ukuran karena mengandung banyak komponen dan gaya bawaan. Kustomisasi Bootstrap dapat memakan waktu, tetapi bisa memilih untuk menyesuaikan komponen yang diperlukan.
    * **Tailwind CSS:**
        * Tailwind adalah alat yang lebih fleksibel yang memberikan kontrol yang lebih besar atas desain. Tailwind tidak memiliki komponen pra-didesain dan lebih berfokus pada penggunaan kelas-kelas kecil untuk membangun tampilan sesuai kebutuhan.

        * Tailwind menggunakan banyak kelas CSS yang bisa ditambahkan langsung ke elemen HTML. Hal ini membuat markup HTML menjadi lebih kaya kelas, tetapi memberi kontrol yang lebih besar atas tampilan dan perilaku elemen tersebut.

        * Tailwind lebih kecil dalam ukuran dan memberi fleksibilitas penuh untuk merancang tampilan sesuai kebutuhan. Kustomisasi dalam Tailwind dapat lebih mudah karena dapat menentukan kelas-kelas sendiri.
    * **Kapan Sebaiknya Menggunakan Bootstrap dan Tailwind CSS:**

        * **Gunakan Bootstrap Jika:**
            * Anda memerlukan pembuatan cepat tampilan dengan komponen yang sudah jadi.
            * Anda tidak memiliki banyak waktu untuk merancang tampilan dari awal.
            * Anda ingin memastikan tampilan yang konsisten di berbagai proyek.
            * Anda tidak memerlukan fleksibilitas desain yang tinggi.
        * **Gunakan Tailwind CSS Jika:**
            * Anda ingin memiliki kontrol yang tinggi atas desain dan tampilan.
            * Anda ingin membangun tampilan yang unik dan tidak ingin bergantung pada desain bawaan.
            * Anda tidak keberatan menambahkan banyak kelas dalam markup HTML Anda.
            * Anda ingin framework yang lebih ringan dan dapat disesuaikan.<br><br>

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

    **Jawaban:**

    1. **Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.**
        1. Sebelum memulai proses desain, saya telah menyisipkan Bootstrap ke dalam template base.html. Hal ini memungkinkan penggunaan framework Bootstrap untuk mempermudah dan mempercantik desain halaman.
        
        2. Pada halaman login, saya menambahkan latar belakang dari gambar yang diambil dari internet, kemudian saya menggunakan Bootstrap untuk melakukan layouting yang rapi. Saya memposisikan "container" logout di tengah halaman dan memberikan padding serta margin yang sesuai untuk setiap elemennya. Saya juga memperindah desain tombol dengan menggunakan Bootstrap dan menghilangkan kata-kata "Username:" dan "Password:" yang redundan.

        3. Pada halaman register, pendekatan yang saya ambil serupa dengan halaman login, hanya saja tidak menggunakan gambar latar belakang melainkan latar belakang berwarna hitam yang telah saya tambahkan secara default pada base.html. Untuk membuat tampilan lebih elegan, saya menggunakan komponen "card" dari Bootstrap. Saya juga dengan teliti mengatur padding dan margin agar tampilan terlihat seimbang, dan mempercantik tampilan tombol dengan memanfaatkan fitur Bootstrap. Dengan demikian, hasilnya adalah halaman register yang terstruktur dengan baik dan memiliki desain yang menarik.

        4. Pada halaman tambah inventori (Add New Item), saya juga telah menerapkan desain menggunakan komponen "card" dari Bootstrap. Saya dengan teliti mengatur margin dan padding untuk memastikan tampilan yang rapi dan seimbang. Tombol "Add Item" juga telah diberi perhatian khusus agar terlihat estetis dan sesuai dengan desain keseluruhan.

    2. **Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.**
        1. Pada halaman daftar inventori ini, saya telah menambahkan tombol "Edit" dan halaman yang sesuai, serta tombol "Delete" sesuai dengan tutorial 4 tanpa perlu menjelaskannya secara detail. Selanjutnya, saya menambahkan navigation bar pada bagian atas halaman dengan judul dan tombol "Logout" untuk memudahkan navigasi. Selain itu, saya menggabungkan nama dan kelas pada kalimat "Welcome" untuk memberikan tampilan yang lebih kompak dan mendesain tabel dengan menggunakan Bootstrap agar terlihat lebih menarik. Saya juga mengatur ukuran font untuk semua teks agar sesuai dengan desain keseluruhan. Semua elemen tersebut saya tempatkan dalam container agar terpusat dan memberikan padding serta margin agar tampilan terlihat lebih rapi. Selain itu, saya juga memperindah desain tombol "Edit", "Delete", "Logout", dan "Add New Item" agar lebih estetis dan sesuai dengan desain yang diinginkan. Dengan demikian, halaman daftar inventori ini memiliki tampilan yang terstruktur, estetis, dan nyaman digunakan.

        2. Saya juga telah merancang halaman Edit item untuk memberikan tampilan yang lebih estetis dengan menggunakan komponen "card" dari Bootstrap. Selain itu, saya telah dengan cermat mengatur posisi, margin, dan padding elemen-elemen pada halaman tersebut.