from fastapi import FastAPI
app = FastAPI()

#기능 만들기 - 기본틀
# @app.get("/") (괄호 안에 바꿔주기)
# def 작명():
#     return something

# 메인 페이지 접속시 'hello' 라는 메시지 보내기
@app.get("/")
def say_hello():
    return "Hello World"