# Praktikum_Search_Algorithms
Raja Naufal Fadhil_2306020

## Deskripsi
Repository ini menyajikan implementasi berbagai algoritma pencarian dalam Python, khususnya pencarian tanpa informasi tambahan (*uninformed search*), yang mencakup:

- **DFS (Depth First Search)**: Menelusuri graph dengan pendekatan menyelam lebih dalam ke cabang sebelum kembali ke node sebelumnya.
- **BFS (Breadth First Search)**: Menelusuri graph secara melebar dengan mengunjungi semua node pada satu tingkat sebelum berpindah ke tingkat berikutnya.
- **UCS (Uniform Cost Search)**: Menemukan jalur optimal berdasarkan bobot atau biaya antar node.

Algoritma-algoritma ini digunakan untuk menemukan jalur dalam graph dengan berbagai pendekatan, baik tanpa informasi tambahan (*uninformed*) maupun dengan informasi heuristik (*informed*).

## Struktur Repository
- `dfs.py` → Implementasi *Depth First Search*
- `bfs.py` → Implementasi *Breadth First Search*
- `ucs.py` → Implementasi *Uniform Cost Search*

Setiap file berisi kode implementasi serta contoh penggunaan yang dapat langsung diuji.

##  Cara Menjalankan di Google Colab
1. Clone repository ini ke Google Colab atau komputer lokal:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```
2. Jalankan file Python yang diinginkan:
   ```bash
   python dfs.py
   python bfs.py
   python ucs.py
   ```

