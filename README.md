# Thiệp Mời Sinh Nhật - Lưu Trung Nghĩa

## 🎉 Link thiệp mời đã deploy

**Live URL:** https://thiep-moi-delta.vercel.app/

## 📋 Danh sách link cho từng khách mời

### 1. Hậu Môn
```
https://thiep-moi-delta.vercel.app/?guest=hau-mon
```

### 2. Thanh Bình - Anh Thư
```
https://thiep-moi-delta.vercel.app/?guest=thanh-binh-anh-thu
```

### 3. Võ Thành - Mai Uy
```
https://thiep-moi-delta.vercel.app/?guest=vo-thanh-mai-uy
```

### 4. Phương Duyên
```
https://thiep-moi-delta.vercel.app/?guest=phuong-duyen
```

### 5. Chu Lai
```
https://thiep-moi-delta.vercel.app/?guest=chu-lai
```

### 6. Nguyên Vũ
```
https://thiep-moi-delta.vercel.app/?guest=nguyen-vu
```

### 7. Cả Nhóm
```
https://thiep-moi-delta.vercel.app/?guest=ca-nhom
```

---

## 🚀 Thông tin deploy

- **Platform:** Vercel
- **Repository:** https://github.com/NghiaLuuu/ThiepMoi
- **Deploy URL:** https://thiep-moi-delta.vercel.app/

## 📱 Test local

Mở file với server local:

```bash
python3 -m http.server 8000
```

Sau đó truy cập: `http://localhost:8000/?guest=hau-mon`

## ✏️ Thêm khách mới

Mở `index.html`, tìm phần `guestMap` trong JavaScript và thêm:

```javascript
const guestMap = {
    'ten-khach': 'Tên Hiển Thị',
    // ...
};
```

URL sẽ là: `https://thiep-moi-delta.vercel.app/?guest=ten-khach`
