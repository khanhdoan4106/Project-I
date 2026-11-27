# Dữ liệu

## Facebook (SNAP)

Nguồn: https://snap.stanford.edu/data/ego-Facebook.html

Mạng bạn bè trên Facebook đã được ẩn danh, gồm 4.039 người (nút) và 88.234 quan hệ bạn bè (cạnh, vô hướng). Mỗi dòng trong file là một cạnh dạng `u v`.

File `data/facebook_combined.txt` đã có sẵn trong repo nên không cần tải lại. Nếu muốn tải lại từ SNAP thì chạy từ thư mục gốc của repo:

```powershell
python scripts/download_data.py
```

Script tải file nén về `data/raw/` (đã có thì không tải lại, thêm `--force` để tải lại), giải nén ra `data/facebook_combined.txt` rồi kiểm tra lại số nút và số cạnh. Thư mục `data/raw/` đã được bỏ qua trong `.gitignore` nên file nén không bị đẩy lên repo.
