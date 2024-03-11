# Docker

## Docker란?

- container technology

### Container

A standardized unit of software

- 패키지와 dependencies를 저장
- 버전 관리

## 가상 환경 vs Docker 컨테이너

### 가상환경

- 독립적으로 공간을 구성할 수 있지만 중복복제로 공간이 낭비되고 매번 새로구성해야하는 단점이 존재
  - 도커를 사용하면 단점을 해결할 수 있다

## Docker 설치 (for Windows)

- WSL2 설치

```shell
wsl --install
```

```shell
wsl --set-default-version 2
```

- [Docker Desktop 설치](https://www.docker.com/products/docker-desktop/)

### 설치 확인
```shell
docker ps
# 이렇게 뜨면 정상적으로 설치됨
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## 컨테이너 실행
### 이미지 생성
- [Dockerfile 작성](./01_intro/Dockerfile)
```bash
docker build .

# 빌드가 완료되면 이미지 아이디를 반환
=> => writing image sha256:292f13437c6c0f8d2d1b8754d820742f0a3cba185fa35e4678661c53c784f8ab  
```

### 컨테이너 실행
```bash
docker run -p 3000:3000 <이미지 ID>
# 3000 포트에 3000 포트를 게시
```

### 컨테이너 종료
```bash
# 컨테이너 목록 확인
docker ps

CONTAINER ID   IMAGE          COMMAND                   CREATED              STATUS              PORTS                    NAMES
1ae0a3b47c48   292f13437c6c   "docker-entrypoint.s…"   About a minute ago   Up About a minute   0.0.0.0:3000->3000/tcp   naughty_thompson
```
```bash
# docker stop <NAMES>
docker stop naughty_thompson
```