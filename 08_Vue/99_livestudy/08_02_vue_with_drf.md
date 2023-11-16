# 11/15 강의
## DRF Authentication
### Authentication (인증)
- Permissions (권한)
    - 요청에 대한 접근 허용 또는 거부 여부를 결정

#### 인증과 권한
- 인증이 먼저 진행

#### DRF에서의 인증
- 인증은 항상 view함수 시작 시,
- 권한 및 제한 확인이 발생하기 전,
- 다른 코드가 실행되기 전

#### 승인되지 않은 응답 및 금지된 응답
1. HTTP 401 Unauthorized
    - 자격 증명이 없기 때문에 인증이 안됨
2. HTTP 403 Forbidden
    - 인증은 되었지만 권한이 없음

### 인증 체계 설정 방법
1. 전역 설정
    - settings.py
    - DEFAULT_AUTHENTICATION_CLASSES
2. View 함수 별 설정
    - authentication_classes 데코레이터

#### DRF가 제공하는 인증 체계

#### TokenAuthentication

### TokenAuthentication 설정
#### 1. 인증 클래스 설정
- 모든 view함수가 토큰 기반 인증이 진행될 수 있도록 설정

### Dj-Rest-Auth 라이브러리

### Token 발급 및 활용

## Authentication with Vue
