# Django

> SSAFY 10기 Django 과정 라이브 강의 코드

| 진행일 | 주제                    |
| ------ | ----------------------- |
| 09/12  | Intro & Design Pattern  |
| 09/13  | Template & URLs         |
| 09/14  | Model                   |
| 09/15  | ORM                     |
| 09/25  | ORM with View           |
| 09/26  | Form                    |
| 09/27  | Static                  |
| 10/4   | Authentication System 1 |
| 10/5   | Authentication System 2 |
| 10/18  | Django REST Framwork 1  |
| 10/19  | Django REST Framwork 2  |

# 시작하기 전에..

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git으로 관리 중
    - TIL/**/*.py
    - git으로 관리 되지 않아야 할 목록
        - .gitignore: 가상환경 생성 (git으로 관리 X)

## 가상환경
- git으로 관리 안함 -> .gitignore
- requirements.txt -> 해당 프로젝트를 위한 독립 환경 목록 구성

## 가상환경 생성
```bash
# 작업 위치 확인
# -m 모듈로 venv 모듈 써서 venv 폴더에 가상환경 만들기
$ python -m venv venv
```

## 가상환경 실행
```bash
$ ls
{folder_name} /    # 생성됐는지 확인

$ source {folder_name}/Scripts/Activate

( folder_name )
$ pip list
```

## Django설치
```bash
$ pip install django
```