<template>
  <div>
    <input type="text" ref="ssafy">
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

// 변수 명은 템플릿 ref 값과 일치
// 안에 들어가는 ref값에 상관없이 호출하면 사용 가능
const ssafy = ref()

onMounted(() => {
  console.log(ssafy.value)
})


</script>

<style scoped>

</style>