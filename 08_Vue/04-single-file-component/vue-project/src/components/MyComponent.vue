<template>
  <!-- 모든 컴포넌트는 최상위 태그 하나만 가짐 -->
  <div>
    <h2>MyComponent</h2>
    <MyComponentItem />
    <MyComponentItem />
    <MyComponentItem />
  </div>
</template>

<script setup>
import MyComponentItem from '@/components/MyComponentItem.vue'

</script>

<style scoped>

</style>