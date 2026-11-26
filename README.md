# Phân tích mạng xã hội và phát hiện cộng đồng

Đây là repo Project 1 của mình. Đề tài là tự cài đặt các thuật toán trên đồ thị để phân tích một mạng xã hội: tìm các nhóm người liên thông, đường đi ngắn nhất giữa hai người, đo xem ai là người quan trọng trong mạng (Degree, Closeness, Betweenness, PageRank) và chia mạng thành các cộng đồng bằng thuật toán Louvain. Thư viện NetworkX chỉ dùng để đối chiếu xem kết quả mình tự cài có đúng không.

Dữ liệu thử nghiệm gồm mạng Karate Club (có sẵn trong NetworkX) và bộ dữ liệu Facebook ego network của SNAP (xem [data/README.md](data/README.md)).

## Cấu trúc thư mục

```
src/sna/     mã nguồn các thuật toán
tests/       các file test chạy bằng pytest
data/        dữ liệu (dữ liệu thô để trong data/raw/, không đẩy lên repo)
```

## Cài đặt và chạy test (Windows)

Cần cài Python 3.11 trở lên. Mở PowerShell trong thư mục repo rồi chạy lần lượt:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest
```

Nếu PowerShell báo không cho chạy script khi kích hoạt venv thì chạy lệnh này một lần rồi kích hoạt lại:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Mỗi lần push hoặc mở PR, GitHub Actions sẽ tự chạy pytest trên Python 3.11.

## Kế hoạch thực hiện

| Tuần | Thời gian | Công việc | Kết quả dự kiến |
|---|---|---|---|
| 1 | 23–29/11 | Xử lý dữ liệu. Hoàn thiện BFS, DFS để tìm các nhóm người liên thông và đường đi ngắn nhất giữa hai người. Tính Degree và Closeness. | Kết quả giống thư viện NetworkX. |
| 2 | 30/11–6/12 | Cài đặt Betweenness và PageRank để đo mức độ quan trọng của mỗi người, chạy thử trên mạng Karate Club. | Kết quả khớp với NetworkX. |
| 3 | 7–13/12 | Cài đặt Louvain để chia mạng thành các cộng đồng, đánh giá bằng modularity. Tải và xử lý bộ dữ liệu Facebook của SNAP, đo thời gian chạy khi mạng lớn dần. | Modularity trên Karate Club từ 0,41 trở lên; có bảng thời gian chạy. |
| 4 | 14–20/12 | So sánh cách các chỉ số xếp hạng mọi người, xem nhóm đứng đầu của từng chỉ số trùng nhau đến đâu. Viết báo cáo thực nghiệm. | Trả lời được câu hỏi người nhiều bạn nhất có phải người ảnh hưởng nhất không; báo cáo hoàn chỉnh. |
| 5 | 21–27/12 | Làm trang web đơn giản: vẽ mạng lưới, tô màu cộng đồng, đánh dấu đường đi, bảng xếp hạng. | Trang web chạy được, xem đủ các kết quả trên. |
| 6 | 28/12–3/1 | Mở rộng: mô phỏng lan truyền thông tin, dự đoán cặp người sẽ kết bạn, kiểm tra độ bền của mạng khi mất dần một số người. | Có kết quả chạy thử, bổ sung vào báo cáo. |
