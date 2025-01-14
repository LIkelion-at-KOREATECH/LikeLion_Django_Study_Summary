## 1주차 - 2. Http Request & Response

### Http
웹상에서 통신을 주고받을 수 있는 주체는 크게 **Client**와 **Server**<br/>
**Server**의 역할은 받은 **Request**를 잘 **가공**해서 **처리**해주는 역할<br/>
Web상에서 지원하는 **통신 규약**을 **Http**라고 한다.<br/>

### Django에서 Http Method

| GET                      | POST                              |
| ------------------------ | --------------------------------- |
| 가져다줘                 | 처리해줘                          |
| URL에 데이터 정보를 포함 | URL에 데이터 정보를 포함하지 않음 | 

Blog프로젝트의 `http://127.0.0.1:8000/new`의 페이지에서<br/>
`GET`방식은 빈 입력공간을 **가져**왔고 `POST`방식은 입력한 내용을 **처리**했다.<br/>
**같은 url**에서 **다른 Http Method**를 사용할 경우 **처리**하는 내용이 **다를 수** 있다.<br/>

### Django Rest Framework에서 Http Method

| Method | 기능                                   |
| ------ | -------------------------------------- |
| GET    | 요청받은 URI의 정보 검색하여 응답한다. |
| POST   | 요청된 자원을 생성(CREATE)한다.        |
| PUT    | 요청된 자원을 수정(UPDATE)한다.        |
| DELETE | 요청된 자원을 삭제한다.                |
| PATCH  | 요청된 자원의 일부를 교체(수정)한다.   |
| OPTION | 웹서버에서 지원되 메소드의 종류 확인   | 

### 예시 1
`http://example.com/post`라는 URL이 존재한다 가정하고<br/>
해당 URL은 글들의 목록을 띄워주는 기능을 갖는 페이지다.<br/>

해당 URL에 `GET`으로 요청을 보냈을 때 서버는 글들의 **목록을 반환**한다.<br/>
`POST`로 요청을 보냈을 때는 **새로운 글 작성**하도록 한다.<br/>

예시의 URL이 글의 목록을 띄워주는 URL일 경우 `PUT`과 `PATCH`와 같은<br/>
**Http Method**를 가지고 있을 필요가 없다.<br/>
모든 URL이 모든 **Http Method**를 가지고 있을 필요가 없다.<br/>

### 예시 2
`http://example.com/post/1`라는 URL을 예시로 들어보면<br/>
해당 URL에 `GET`요청을 보낼 경우 **1번 글을 반환**할 것이다.<br/>
해당 URL에 `DELETE`요청을 보낼 경우 **1번 글을 삭제**할 것이다.<br/>
해당 URL에 `PUT/PATCH`요청을 보낼 경우 **1번 글을 수정**할 것이다.<br/>

위의 URL에서는 `POST`요청은 존재할 필요가 없다.<br/>

### Http Response
**Django Rest Framework API Server**에서는 **JSON**을 주고받는다.<br/>
서버의 **Response**에는 아래와 같은 종류가 존재한다.<br/>

- **1**XX (**정보**)
    - 요청을 받았으며 프로세스를 계속한다.
- **2**XX (**성공**) :
    - 요청을 성공적으로 받았으며 인식했고 수용했다.
- **3**XX (**리다이렉션**) :
    - 요청을 완료하기 위해 추가 작업 조치가 필요하다.
- **4**XX (**클라이언트 오류**) :
    - 요청의 문법이 잘못되었거나 요청을 처리할 수 없다.
- **5**XX (**서버 오류**)
    - 서버가 명백히 유요한 요청에 대해 충족에 실패했다.
