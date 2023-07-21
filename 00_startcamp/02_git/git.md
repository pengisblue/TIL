# GIT 이란
> 분산 버전 관리 시스템

## Git 의 3가지 영역
1. Working Directory
    - 실제 작업 영역
2. Staging Area
    - 다음 버전을 준비할 수 있는 중간 준비 영역
    - 수정 사항 기록
3. Repository
    - 버전(commit)이력과 파일이 저장되는 영역

## Git 시작하기
### git 초기화
```bash
$ git init  #작업 위치 확인하기
```

### git 기초 설정
```bash
$ git config --global user.email "khi762@naver.com"
$ git config --global  user.name "김해인"

$ git config --global --list 
```

### 상태 확인 명령어
```bash
$ git status
```

### staging area에 추가 (wd -> sa)
```bash
$ git add {path}<folder_name>/{file_name}
$ git add . #현재 폴더안에 있는 전부 add
```
```bash
# add된 파일 삭제
$ git rm --cached {file_name}
```

### Repository에 저장하기
```bash
$ git commit -m "commit message"  # -m : message
```

- #### 파일을 수정했을 때
     add -> commit 과정 반복

### 커밋 기록 확인하기
```bash
$ git log
$ git log --oneline #log 요약
```

### 직전 커밋 수정하기
```bash
$ git commit --amend
# vim에서 커밋 내용 수정하기
# 1. insert: - 삽입 상태 만들기
# 2. 커밋 메시지를 수정한다.
# 3. esc: - 삽입 상태를 종료
# 4. :wq (write quit): 저장하고 종료
```

### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# 1. vim git 설정 파일 열기
$ vim ~/.gitconfig
# 2. insert 키: 수정 상태 만들기
# 3. --insert-- 인 상태에서 모든 내용 삭제
# 4. esc: 수정 상태 종료
# 5. :wq
```
```bash
# vscode로 제거하기
$ code ~/.gitconfig
```
```bash
# 명령어로 제거하기
$ git config --global --unset-all core.editor
```

### vim 명령어
1. Insert : 수정 상태 만들기
2. esc : 커서를 제일 밑으로 이동
3. Ctrl + U : 한 줄 지우기
4. U : 이전으로
5. :q, :wq : quit, write and quit

### github에 Repository추가하기
```bash
# 1. New 클릭
# 2. Repository name 정하기
# 3. Public or Private
# 4. remote 주소를 추가하기
$ git remote add origin https://github.com/pengisblue/TIL.git
# 5. remote 확인
$ git remote -v
# 6. 원격저장소에 push
$ git push origin master
```

### 원격 저장소 git에 등록
```bash
$ git remote add {remote_nickname} {remote_url}
```

### 원격 저장소에 업로드
```bash
$ git push origin master    # origin : remote_nickname master : branch
```

### 원격 저장소에 있는 내용 복제
- 최초로 내려 받을 때
```bash
$ git clone {remote_url}
```
- 내려 받을 때
```bash
$ git pull origin master
```

### git ignore
- git에서 탐색하지 않을 파일, 폴더 목록
- .gitignore 파일에 상대경로로 파일, 폴더명 작성
- [gitignore.io](https://www.toptal.com/developers/gitignore/)에서 쉽게 생성 가능