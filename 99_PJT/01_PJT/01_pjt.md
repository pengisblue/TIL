# 공통 이론
## requests 모듈
```python
import requests

request.get(url)  # 해당 서버(url)에 데이터를 달라고 요청하는 함수

.json()  # 내부 데이터를 JSON 형태로 변환해주는 함수

```

## API
- 클라이언트가 원하는 기능을 수행하기 위해서 서버 측에 만들어 놓은 프로그램
- 서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 API를 미리 만들어 둠

### OPEN API
> 외부에서 사용할 수 있도록 무료로 개방된 API  
> 사용법은 Docs에 명시
- 오픈 API 예시
    - OpenWeatherMap API: 기상 데이터 및 날씨 정보를 제공 오픈 API
    - 금융상품통합비교공시 API: 금감원에서 제공하는 금융 상품 정보 제공 오픈 API

### API가 사용하는 데이터 형식 - JSON
- JavaScript Object Notation '자바스크립트 객체 표기법'
- 경량의 텍스트 기반의 데이터 형식
- 문법 X 데이터 표현 방법 O
- 특징
    - '{}'로 둘러싸인 키-값 쌍의 집합
    - 키 = 문자열 / 값 = 다양한 데이터 유형
    - 값은 쉼표로 구분
- 참고
    - 파싱(Parsing): 데이터를 의미 있는 구조로 분석하고 해석하는 과정
    - json.loads(): JSON 형식의 문자열을 파싱하여 python Dictionary로 변환
```python
import json  # 내장 모듈

# json 데이터
json_data = '''
{
    "name": "김싸피",
    "age": 28,
    "hobbies": [
        "공부하기",
        "복습하기"
    ]
}
'''

# JSON 데이터(문자열) -> dict
data = json.loads(json_data)  

print(data)  # {'name': '김싸피', 'age': 28, 'hobbies': ['공부하기', '복습하기']}

# JSON 데이터에서 원하는 데이터만 가져오기
name = data.get('name')

print(name)  # 김싸피
```

## [OpenWeatherMap API](https://openweathermap.org/api)

## jupyter notebook
```bash
# 설치
$ pip install notebook
```
```bash
# 실행 단축키 변경 (jp)
$ code ~/.bashrc

alias jp="jupyter notebook"  # bash로 설치
alias jp="puthon -m notebook"  # cmd로 설치
```