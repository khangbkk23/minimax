# 🏆 Trò chơi Cờ Vây (5x5) & Cờ Caro (3x3) - Minimax AI

Đây là một dự án Python sử dụng **Pygame** để phát triển hai trò chơi:

- **Cờ Vây (5x5)**: Người chơi đấu với AI, trong đó AI sử dụng thuật toán **Minimax** có cắt tỉa **Alpha-Beta** để đưa ra nước đi tối ưu.
- **Cờ Caro (3x3)**: Trò chơi đơn giản hơn nhưng vẫn áp dụng Minimax để đảm bảo AI chơi tối ưu.

---

## 📌 Cách cài đặt và chạy

### 1️⃣ Cài đặt thư viện cần thiết
Bạn cần cài đặt **Python** (từ 3.7 trở lên) và thư viện **Pygame**:
```sh
pip install pygame
```

### 2️⃣ Chạy từng trò chơi
- Chạy **Cờ Vây (5x5)**:
  ```sh
  python go_game.py
  ```
- Chạy **Cờ Caro (3x3)**:
  ```sh
  python tic_tac_toe.py
  ```

---

## 🎮 Luật chơi

### 1️⃣ Cờ Vây (5x5)
- Người chơi (màu trắng) đi trước, AI (màu đen) đi sau.
- Trò chơi kết thúc khi tất cả các ô trên bàn cờ được lấp đầy.
- Người chơi có nhiều quân cờ hơn sẽ thắng.

### 2️⃣ Cờ Caro (3x3)
- Người chơi (X) đi trước, AI (O) đi sau.
- Người chiến thắng là người có 3 quân thẳng hàng (ngang, dọc hoặc chéo).
- Trò chơi kết thúc khi có người thắng hoặc bàn cờ đầy (hòa).

---

## 🤖 AI và thuật toán Minimax

Cả hai trò chơi đều sử dụng thuật toán **Minimax** với cắt tỉa **Alpha-Beta** để tối ưu hoá nước đi của AI. Minimax hoạt động như sau:

1. AI giả lập tất cả các nước đi có thể.
2. Đánh giá điểm số cho từng trạng thái dựa trên số quân cờ kiểm soát được.
3. Dự đoán nước đi của đối thủ và điều chỉnh chiến thuật.
4. Chọn nước đi mang lại lợi thế lớn nhất.

Ở trò chơi Cờ Vây, AI tìm cách tối đa hóa số quân của mình, còn trong Cờ Caro, AI cố gắng chiến thắng hoặc cầm hòa nếu không có nước đi tốt.
