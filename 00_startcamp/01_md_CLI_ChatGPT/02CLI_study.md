# CLI
- Command Line Interface

- 새폴더 만들기
```bash
$ mkdir new_ folder #make directory
```

- 작업 위치를 new_folder로 이동
```bash
$ cd new_folder #change directory
```

- 현재 작업 위치를 열기 (파일 열기)
```bash
# . : 현재 위치 (상대 경로)
$ start .

# 현재 폴더를 vscode로 열기
$ code .

# 현재 폴더에 있는 파일을 vscode로 여기 / vscode 파일 만들기
$ code README.md # README.md 파일이 열림 / 없는 파일명 입력 시 파일 생성(저장하면)
```

- 현재 작업 위치의 파일 목록
```bash
$ ls
```

- 숨긴 파일 보기
```bash
$ ls -a #all(show hidden files)
```

- 파일의 이름을 바꾸거나 위치를 옮기거나
```bash
$ mv {이동할 대상} {이동될 위치} # .. : 상위 폴더
$ mv {이름 바꿀 대상} {바꿀 이름}
```


### - 상대 경로, 절대 경로
1. 절대 경로
    - /c/Users/SSAFY/Desktop/new_folder
```bash
$ pwd # print working directory
```

2. 상대 경로
    - 내 위치를 기준으로 경로를 이동

    - 삭제
```bash
$ rm {파일명}
$ rm -r {폴더}
# 복구가 안된다
```

### - 명령어
1. double-dash (--)
    - 축약없는 표준 그대로 옵션에 입력하는 경우
```bash
# --option
$ --help 
```
2. one-dash (-)
    - 축약된 형태, 문자 하나하나에 대한 동작을 순서대로 수행
```bash
# -option
$ ls -al # -al : -a / -l(long output) 순서대로 실행
```
3. 재귀 (-r)