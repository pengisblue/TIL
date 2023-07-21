// 채팅 전송 및 수신을 위한 선택
const chatInput = document.querySelector(".chat-input")
const chatSubmitIcon = document.querySelector(".chat-submit-icon")
const chatContainer = document.querySelector(".chat-area")


// 채팅창에 내용을 추가해주는 부분
const addChat = (type, value) => {
  const chat = document.createElement("div")
  chat.classList.add("chat")
  chat.innerText = value
  chat.classList.add(`${type}-chat`)
  chatContainer.appendChild(chat)
  chatContainer.scrollTop = chatContainer.scrollHeight
}

// 1. 챗봇 서버에 요청할 URL (chatGPT API reference Chat 파트 참고)
const OPEN_API_URL = "https://api.openai.com/v1/chat/completions"
// 2. API 키 (발급 받은 Secret Key)
const API_KEY = "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"

// 필요한 헤더 정보
const headers = {
  'Authorization': `Bearer ${API_KEY}`, // 인증 키 설정
  'Content-Type': 'application/json'    // 요청 데이터의 타입
}

// 이전에 응답받은 메세지를 저장하는 변수
let oldMsg = ''

const chatReceive = (userMsg) => {
  // 사용자가 입력한 내용은 content 에 작성하여 API 서버에 전달
  const messages = [
    // 사용자가 작성한 내용에 대한 부분
    {
      'role': 'user',
      'content': userMsg,
    },
    // 이전에 응답한 내용을 아래와 같이 넣어주지 않으면 챗팅 맥락이 연결되지 않음
    // 1. 이전 정보를 메세지에 추가
    {
      'role': 'system',  
      'content': oldMsg
    }
  ]

  // chatGPT API 서버에 요청을 보내는 부분
  axios({
    // 요청에 대한 설정 부분
    'method': 'post',           // POST 요청
    'url': OPEN_API_URL,        // 요청하는 URL 
    'headers': headers,         // 인증 데이터 설정
    'data': {                   // 요청 데이터 설정
      'model': 'gpt-3.5-turbo',   // gpt 모델 정보 설정
      'messages': messages,       // 사용자가 입력한 내용을 담은 메세지 설정
    }
  })
  //  chatGPT API 서버에서 정상적으로 응답이 도달했을 때 실행되는 부분
  .then( res => {
    // 응답 데이터 확인 (크롬 개발자 도구 콘솔창)
    console.log(res.data)

    // 1. 응답 데이터에서 응답 메세지를 가져온다.
    response = res.data.choices[0].message.content

    // 2. 챗팅창에 메세지를 등록한다.
    addChat("receive", response)
     

    // 3. 챗팅의 연속성을 위해 이전 메세지를 oldMsg 변수에 저장
    // messages 에서 system 메세지의 content 값으로 설정됨
    oldMsg = response
    
  })
  // 요청에 있어 잘못된 설정이나 서버에 문제가 있을 때 실행되는 부분
  .catch(err => {
    console.log(err.response.data)    // 에러 데이터
    console.log(err.response.status)  // 4xx : 사용자 실수, 5xx : 서버 문제 
  })

}


const chatSubmit = () => {
  const value = chatInput.value
  if (!value) return
  addChat("send", value)
  chatReceive(value)
  chatInput.value = ""
}

chatInput.addEventListener("keyup", (e) => {
  e.key === "Enter" && chatSubmit()
})