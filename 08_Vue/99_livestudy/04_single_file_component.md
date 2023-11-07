# 11/7 강의
## Single-File Components
### Component
- 재사용 가능한 코드 블록
- 특징
    - UI를 독립적이고 재사용 가능한 일부분으로 분할하고 개별적으로 다룰 수 있음
    - 앱은 자연스럽게 중첩된 Component의 트리로 구성됨

### SFC (Single-File Components)
- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 (`*.vue`)
- \<template>, \<script>, \<style> 블록으로 구성 

#### 컴포넌트 사용하기
- Vue SFC는 컴파일러를 통해 컴파일 된 후 빌드 되어야 함
    - Vite 사용

## SFC build tool ([Vite](https://vitejs.dev/))
### Vite

### NPM (Node Package Manager)
- Node.js의 기본 패키지 관리자
- Node.js
    - JavaScript 엔진을 기반으로 하는 Serveer-Side 실행 환경
    - 프론트와 백에서 동일한 언어로 개발이 가능

### Vite 프로젝트 구조
#### node_modules

#### package-lock.json

#### public 디렉토리
- root 절대 경로를 사용하여 참조
- 컴포넌트에서 직접적으로 사용하지 않는 정적 파일

#### src 디렉토리
- src/assets
    - 프로젝트 내에서 사용되는 자원(이미지, 폰트, 스타일 시트 등)

- src/components

- src/App.vue
    - Root 컴포넌트
    - 다른 하위 컴포넌트들을 포함
    - 애플리케이션 전체의 레이아웃과 공통적인 요소를 정의

- src/main.js
    - Vue 인스턴스를 생성하고 애플리케이션을 초기화하는 역할
    - 필요한 라이브러리를 import
    - 전역 설정 수행

#### index.html
- Root 컴포넌트인 App.vue가 해당 페이지에 마운트 됨
    - Vue 앱이 SPA인 이유

### 모듈과 번들러
#### Modue
- 프로그램을 구성하는 독립적인 코드 블록 (*.js파일)

#### Bundler
- 복잡하고 깊은 모듈의 의존성 문제를 해결하기 위한 도구
- 의존성 관리, 코드 최적화, 리소스 관리

## Vue Component
### Component 활용
1. 컴포넌트 파일 생성
2. 컴포넌트 등록(import)

#### [Component 이름 스타일 가이드](https://ko.vuejs.org/style-guide/rules-strongly-recommended.html)

## 추가 주제
### Virtual DOM
- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념

#### Virtual Dom 장점

#### Virtual Dom 주의사항
- 실제 DOM에 직접 접근 X
    - querySelector, createElement, addEventListener 등

#### 직접 DOM 엘리먼트에 접근해야 하는 경우
- ref 속성을 사용하여 특정 DOM 엘리먼트에 직접적인 참조 가능

### Composition API & Option API
- Composition API
    - Vue3에서의 권장 방식
    - 규모가 있는 앱의 전체를 구축
- Option API
    - Vue2에서의 권장 방식

## 참고
### Scaffolding (스캐폴딩)
- 초기 구조와 기본 코드를 자동으로 생성하는 과정

### SFC의 CSS기능 - scoped
- scoped를 사용하면 부모 컴포넌트의 스타일이 자식 컴포넌트로 유출되지 않음
- 단, 자식 컴포넌트의 최상위 요소는 부모와 자식의 CSS모두 영향을 받음
    - 부모가 레이아수 목적으로 자식 컴포넌트의 최상위 요소의 스타일을 지정할 수 있도록