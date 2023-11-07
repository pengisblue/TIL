<template>
  <div class="greeting">{{ msg }}</div>
</template>

<script setup>
import { ref } from 'vue'

const msg = ref('hello world!') 
</script>

<style scoped>  /* scoped : 현재 컴포넌트 파일에서만 sytle을 적용 */

.greeting {
  color: red;
}

</style>