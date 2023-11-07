<template>
  <h1>App.vue</h1>
  <MyComponent />
</template>

<script setup>
// 상대경로를 통해 import
// import MyComponent from './components/MyComponent.vue'
// @ : scr/ 절대 경로를 의미
// import MyComponent from 'src/components/MyComponent.vue'
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>
div {
  color: red;
}
</style>