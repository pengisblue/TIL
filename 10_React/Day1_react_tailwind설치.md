# day1 (1월 8일) 학습

## 기획
### 단계
1. 요구사항 분석
2. 개발 기능 정의
3. 프로세스 정리
4. 상세화면 기획

### 1. 요구사항 분석
- 실제 서비스를 쓰는 현업 대상 개발 요구사항 정리
- 확인된 요구 사항에 대한 분석 및 정리 -> 문서화 하여 상세하게, 확실한 컨펌
- 산출물: 요구사항 정의서
    - 요구사항id, 요구사항명, 상세설명, 우선순위, 핵심기능 여부, 담당자

### 2. 개발 기능 정의
- 요구사항 기반 기능 정의

### 3. WBS(Work BreakDown Structure)
- 일정, 담당자! (종료 일정)
- 지연에 대한 이슈를 관리할 수 있음

### 4.1 Flow chart 작성
- 업무 흐름 파악

### 4.2 IA 작성
- 기능 정리 (depth별 정리)

### 5. 화면 기획
- 와이어 프레임
- UI/UX 집중

## React 시작하기
```bash
npx create-react-app 프로젝트이름
```
```bash
cd 프로젝트파일
npm start
```

## tailwind 설치
```bash
npm install -D tailwindcss
npx tailwindcss init
```
```js
// tailwind.config.js content 추가하기
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
}
```
```css
/* src/index.css 수정 */
@tailwind base;
@tailwind components;
@tailwind utilities;
```