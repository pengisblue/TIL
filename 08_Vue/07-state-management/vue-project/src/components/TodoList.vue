<template>
    <div>
      <TodoListItem 
        v-for="todo in store.todos"
        :key="todo.id"
        :todo-data="todo"
      />
    </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
import { useTodoStore } from '../stores/todo'

const store = useTodoStore()


</script>

<style scoped>

</style>