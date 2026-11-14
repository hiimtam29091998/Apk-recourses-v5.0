# KHOÁNG THẠCH MOBILE (Android Studio Project)

**Trạng thái: mã nguồn dự án hoàn chỉnh để biên dịch, CHƯA phải APK đã biên dịch.**

Dự án này giữ nguyên bộ tối ưu **SciPy/HiGHS MILP v5.0** và tích hợp Python vào Android bằng **Chaquopy 17.2**. Không cần máy chủ Python hay Internet sau khi cài đặt APK. Dữ liệu chỉ được lưu trên điện thoại, không có quyền INTERNET trong AndroidManifest.

## Thiết bị mục tiêu

- **Samsung Galaxy S23 Ultra**, bộ xử lý ARM64 (`arm64-v8a`).
- `minSdk=26`, `targetSdk=34`, `compileSdk=35`.
- Giao diện WebView bằng tiếng Việt, hỗ trợ màn hình cảm ứng và chế độ dọc.

## Cách xây APK trên Windows bằng Android Studio

1. Cài **Android Studio** chính thức từ https://developer.android.com/studio. Cài Android SDK Platform 35, Build-Tools 35 và Android SDK Command-line Tools nếu IDE yêu cầu. Mở dự án bằng **File > Open**, chọn thư mục `KHOANG_THACH_Mobile_Android_Studio` (nằm trong ZIP).
2. Dùng **JDK 17** cho Gradle (Android Studio thường cung cấp JDK đi kèm). Gradle khuyến nghị **8.9**; Android Gradle Plugin **8.7.3**; Chaquopy **17.2.0**.
3. Máy tính build cần có **Python 3.11** trên PATH. Chaquopy sẽ cài và đóng gói `numpy`, `scipy`, `xlsxwriter` cho Android ARM64 ở **lần build đầu**. Việc tải Gradle, plugin và Python wheel cần Internet lần đầu.
4. Nếu IDE báo **Gradle wrapper missing**, cài Gradle 8.9 và chạy `gradle wrapper --gradle-version 8.9` tại thư mục dự án, rồi nhấn **Sync Project with Gradle Files**. Gói mã nguồn hiện chưa có `gradle-wrapper.jar` vì môi trường tạo dự án không tải được tệp này.
5. Chọn **Build > Build Bundle(s) / APK(s) > Build APK(s)** (hoặc **Build > Build APK(s)** tùy phiên bản Android Studio).
6. Sau khi build thành công, APK debug sẽ nằm tại `app/build/outputs/apk/debug/app-debug.apk`. Chỉ coi đó là đường dẫn dự kiến, không phải file có sẵn trong gói này.
7. Chuyển APK qua USB hoặc Quick Share tới Galaxy S23 Ultra, mở bằng ứng dụng **My Files** và cài. Android có thể yêu cầu cho phép cài ứng dụng từ nguồn này; chỉ chấp nhận khi bạn tin cậy tệp đã tự biên dịch. Không cần tắt Play Protect.

**Không cần chạy file `.bat` để mở ứng dụng trên điện thoại.** APK đã biên dịch tích hợp đủ giao diện và Python/SciPy.

## Những tính năng đã kết nối với Android

- Lập kế hoạch tới hết 30/04/2028, 76 tuần sự kiện, lịch mở thứ Ba và hạn chót phù hợp.
- 3 bậc tối ưu: ưu tiên cốt lõi, lượt Chợ lấp lánh bổ sung, sau đó tối đa vàng.
- Nhập điểm boss tốt nhất trong tối đa 20 lần; nhập theo tuần, chế độ dự báo cố định/tăng trưởng.
- Hồ sơ nhiều người chơi lưu bằng `localStorage` của WebView (chỉ nội bộ ứng dụng).
- Xuất Excel (.xlsx), ZIP CSV bằng **Android Storage Access Framework**: chọn nơi lưu.
- Sao lưu và khôi phục hồ sơ `.json` bằng bộ chọn tệp Android.
- PDF tiếng Anh, tiếng Trung phồn thể qua giao diện **Print / Save as PDF** của Android.
- Mỗi ngày giao dịch gộp thành một hàng, có thể xem chi tiết, lọc theo năm 2026–2028.

## Dữ liệu và quyền riêng tư

- Không khai báo `android.permission.INTERNET`. Không có backend HTTP trong APK.
- Không yêu cầu quyền đọc/ghi toàn bộ bộ nhớ. Người chơi chủ động chọn tệp khi xuất/nhập.
- `allowBackup=false` tránh sao lưu Android tự động; hãy dùng nút **Sao lưu hồ sơ** để xuất JSON trước khi gỡ app.
- Gỡ cài đặt ứng dụng sẽ xóa hồ sơ đã lưu trong WebView nếu chưa xuất JSON.

## Cấu trúc

- `app/src/main/java/com/khoangthach/mobile/MainActivity.java`: WebView + cầu nối Java/Python, bộ chọn tệp, Android Print.
- `app/src/main/assets/`: HTML/CSS/JS đã điều chỉnh cho màn hình điện thoại.
- `app/src/main/python/optimizer.py`: bộ giải nguyên gốc v5.0; **không viết lại xấp xỉ**.
- `app/src/main/python/android_bridge.py`: cầu nối JSON, xuất Excel/ZIP CSV.
- `app/src/main/python/excel_export.py`, `reporting.py`, `server.py`: bộ tạo báo cáo gốc (server.py chỉ được import để lấy hàm xuất ZIP; không khởi động server).
- `verify_bridge.py`: kiểm tra Python và xuất báo cáo trên máy có Python/SciPy.
- `tests/test_optimizer.py`: 23 bài kiểm thử của bản gốc.

## Những điểm chưa kiểm thử trên Android thật

Đã kiểm thử bộ giải và phần bridge Python trên Linux nhưng **chưa thể build APK hoặc chạy trên Galaxy S23 Ultra** ở môi trường hiện tại (thiếu Android SDK, Gradle và quyền tải phụ thuộc). Vì vậy:

- Cần xác nhận quá trình đóng gói `scipy` cho ARM64 với đúng phiên bản Chaquopy và Android Gradle Plugin.
- Cần kiểm tra hiệu năng MILP khi chạy trên điện thoại thật.
- Cần kiểm tra chức năng JavaScript Bridge, lưu tệp và Print-to-PDF trên WebView/One UI thực tế.
- Nếu Android Studio báo thiếu Python wheel, hãy kiểm tra danh sách phiên bản wheel hỗ trợ tại https://chaquo.com/chaquopy/doc/current/android.html và sửa phiên bản Python/package; **không bỏ SciPy** nếu chưa có phương pháp tương đương được kiểm chứng.

Dự án có thể được kiểm tra trên máy tính bằng `python verify_bridge.py` và `python -m unittest discover -s tests -v` sau khi cài numpy/scipy/xlsxwriter.

## Cách 2: Tạo APK trên GitHub Actions (không cần Android Studio ở máy bạn)

Nếu bạn có tài khoản GitHub:

1. Tạo một repository **riêng tư** mới và đưa **nội dung bên trong** thư mục dự án này vào gốc repository (không đưa cả thư mục cha nếu muốn workflow hoạt động ngay).
2. Vào tab **Actions**, chọn workflow **Build Khoang Thach Android APK**, nhấn **Run workflow**.
3. Khi workflow báo xanh (Build thành công), mở lần chạy đó, kéo xuống **Artifacts**, tải **Khoang-Thach-Mobile-debug-APK**.
4. Giải nén artifact để lấy `app-debug.apk`; chuyển tệp này sang Samsung Galaxy S23 Ultra rồi cài đặt.

Workflow ở `.github/workflows/build-apk.yml`. Đây là **quy trình được cung cấp nhưng chưa thể chạy thử trong môi trường tạo dự án**, không bảo đảm việc build sẽ thành công trước khi kiểm chứng trên GitHub Actions.

### Vì sao không có sẵn APK trong ZIP?

APK phải được biên dịch bằng Android SDK và plugin Gradle, đồng thời nhúng Python/SciPy cho ARM64. Môi trường làm việc hiện tại không có Android SDK/Gradle và không có kết nối tải các phụ thuộc đó. Do vậy, **không có APK đã được xác minh để gửi trực tiếp trong lần này**.
