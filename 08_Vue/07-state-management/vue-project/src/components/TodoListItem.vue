<template>
    <div>
      <span 
        @click="store.updateTodo(todoData.id)"
        :class="{ 'is-done': todoData.isDone }"
      >
        {{ todoData.text }}
      </span>
      <button @click="store.deleteTodo(todoData.id)">X</button>
    </div>
</template>

<script setup>
import { useTodoStore } from '../stores/todo'

defineProps({
  todoData: Object
})

const store = useTodoStore()

</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}

</style>