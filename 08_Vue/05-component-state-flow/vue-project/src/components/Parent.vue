<template>
  <div>
    <!-- html 속성값 : 케밥 케이스 -->
    <ParentChild
      my-msg="ssafy"
      :dynamic-props="name"
      @some-event="someCallback"
      @emit-args="getNumbers"
      @update-name="updateName"
    />
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue'
import { ref } from 'vue'

const name = ref('Alice')

const someCallback = function () {
  console.log('ParentChild가 발신한 emit 이벤트 수신')
}

const getNumbers = function (...args) {
  console.log(args)
}

const updateName = function () {
  if (name.value === 'Alice') {
    name.value = 'Bella'
  } else {
    name.value = 'Alice'
  }
}
</script>

<style scoped>

</style>