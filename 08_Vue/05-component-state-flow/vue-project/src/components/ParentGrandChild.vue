<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ userName }}</p>
    <button @click="updateName">이름 변경</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,
  userName: String,
})

const emit = defineEmits(['updateName'])

const updateName = function () {
  emit('updateName')
}
</script>
<style scoped>

</style>