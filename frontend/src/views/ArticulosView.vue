<template>
  <div>
    <h1>Gestión de Artículos</h1>
    <ArticuloForm />
    <ArticuloList />
  </div>
</template>

<script setup lang="ts">
import ArticuloForm from '@/components/articulos/ArticuloForm.vue'
import ArticuloList from '@/components/articulos/ArticuloList.vue'
</script>