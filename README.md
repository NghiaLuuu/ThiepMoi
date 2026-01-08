# Thiệp Mời Sinh Nhật - Lưu Trung Nghĩa

## 🎉 Cách sử dụng

Deploy file `index.html` lên hosting (Vercel, Netlify, GitHub Pages, v.v.)

## 📋 Danh sách URL cho từng khách mời

Sau khi deploy, thêm parameter `?guest=` vào URL:

### URLs cho từng khách:

1. **Hậu Môn**
   ```
   https://your-domain.com/?guest=hau-mon
   ```

2. **Thanh Bình - Anh Thư**
   ```
   https://your-domain.com/?guest=thanh-binh-anh-thu
   ```

3. **Võ Thành - Mai Uy**
   ```
   https://your-domain.com/?guest=vo-thanh-mai-uy
   ```

4. **Phương Duyên**
   ```
   https://your-domain.com/?guest=phuong-duyen
   ```

5. **Chu Lai**
   ```
   https://your-domain.com/?guest=chu-lai
   ```

6. **Nguyên Vũ**
   ```
   https://your-domain.com/?guest=nguyen-vu
   ```

## 🚀 Cách deploy nhanh

### Option 1: Vercel (Khuyên dùng)
1. Tạo tài khoản tại https://vercel.com
2. Kéo thả folder `ThiepMoi` vào Vercel
3. Deploy tự động, nhận link

### Option 2: Netlify
1. Tạo tài khoản tại https://netlify.com
2. Kéo thả folder vào Netlify Drop
3. Nhận link ngay lập tức

### Option 3: GitHub Pages
1. Tạo repository mới trên GitHub
2. Upload file `index.html`
3. Enable GitHub Pages trong Settings
4. Truy cập: `https://username.github.io/repo-name/`

## 📱 Test local

Mở file với server local (không dùng file://)

```bash
# Python
python3 -m http.server 8000

# Node.js
npx serve

# PHP
php -S localhost:8000
```

Sau đó truy cập: `http://localhost:8000/?guest=hau-mon`

## ✏️ Thêm khách mới

Mở `index.html`, tìm phần `guestMap` và thêm:

```javascript
const guestMap = {
    'ten-khach': 'Tên Hiển Thị',
    // ...
};
```

URL sẽ là: `?guest=ten-khach`
