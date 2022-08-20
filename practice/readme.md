참고자료 :https://wikidocs.net/162345



## 초기 설정

- `python -m venv venv`
- `pip install fastap==0.74.1`
- `pip install "uvicorn[standard]"`

## 서버 만들기

```python
# main.py

from fastapi import FastAPI
app = FastAPI()
```

## 기능 만들기

### 기본 틀

```python
from fastapi import FastAPI
app = FastAPI()

#기능 만들기 - 기본틀
@app.get("/") #괄호 안: 접속 url, 'get': 메소드
def 작명():
    return something
```

### 기능 1

> 메인 페이지 접속시 'Hello World' 출력하기

```python
from fastapi import FastAPI
app = FastAPI()

# 메인 페이지 접속시 'hello' 라는 메시지 보내기
@app.get("/")
def say_hello():
    return "Hello World"
```

## 서버 실행

```bash
$ uvicorn main:app
```

