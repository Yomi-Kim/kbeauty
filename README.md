# 🛒 Django 제품 관리 시스템 과제

## 🚀 기능 개요

### ✅ 1. 제품 목록 (Read/List)
- 등록된 제품 목록을 확인 가능
- **정렬 가능**: 제품 이름순, 최신 등록순
- **검색 가능**: 제품명 기반 검색
- **페이징 지원**: 10개씩 표시되며, 페이지 이동 가능

### ✅ 2. 제품 생성 (Create)
- **입력 필드**: 이름, 가격, 재고, 설명
- **유효성 검사**
  - 제품명: 255자 이하, 공백 불가
  - 가격: 0 이상의 숫자 (소수점 둘째 자리까지)
  - 재고: 0 이상의 정수
  - 설명: 최소 10자 이상
- **입력 오류 발생 시 사용자에게 오류 메시지 표시**
- **등록 후 제품 목록으로 리디렉션**

### ✅ 3. 제품 수정 (Update)
- 기존 제품 정보를 수정 가능
- 생성 시 적용된 **유효성 검사 동일하게 적용**
- 수정 후 제품 목록으로 리디렉션

### ✅ 4. 제품 삭제 (Delete)
- **삭제 모달**을 활용하여 삭제 확인 가능
- 삭제 후 자동으로 목록 업데이트

---

## 🛠️ 기술 스택

### **✅ Backend**
- Django 4.2
- Python 3.9
- PostgreSQL 14.17

### **✅ Frontend**
- HTML, CSS
- Bootstrap 5
- JavaScript (삭제 모달, 검색 필터링)

---

## 🔧 설치 및 실행 방법(MAC)

### 1️⃣ **프로젝트 클론**
```bash
git clone https://github.com/your-repository/django-product-management.git
cd django-product-management
```

### 2️⃣ **가상환경 설정**
```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ **필수 패키지 설치**
```bash
pip install -r requirements.txt
```
### 4️⃣ **환경 변수 설정 (.env)**
.env 파일을 프로젝트 루트 디렉토리에 추가하고 아래와 같이 설정합니다.

```ini
DJANGO_SECRET_KEY=test_secret_key
DEBUG=True

DB_NAME=shop_db
DB_USER=postgres
DB_PASSWORD=postgres_password
DB_HOST=localhost
DB_PORT=5432
```

### **5️⃣ 데이터베이스 설정**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6️⃣ 슈퍼유저 생성 (관리자 계정)**
```bash
python manage.py createsuperuser
→ 사용자명, 이메일, 비밀번호 입력 후 생성
```

### **7️⃣ 서버 실행**
```bash
python manage.py runserver
이후 웹 브라우저에서 http://localhost:8000 접속
```

---

## 📌 주요 URL

|기능|경로|
|---|---|
|제품 목록|/products/|
|제품 생성|/products/create/|
|제품 수정|/products/<int:pk>/update/|
|제품 삭제|/products/<int:pk>/delete/|
|로그인|/accounts/login/|
|로그아웃|/accounts/logout/|

---

## 📜 라이선스
본 프로젝트는 MIT License를 따릅니다.

---

## 📩 문의
문의 사항이 있다면 아래 이메일로 연락 주세요:
📧 minjunkoo1@naver.com
