<template>
  <div>
    <h1>Gestión de Categorías</h1>
    <CategoriaForm />
    <CategoriaList />
</div>
</template>
<script setup lang="ts">
import CategoriaList from '@/components/categorias/CategoriaList.vue';
import CategoriaForm from '@/components/categorias/CategoriaForm.vue';
</script>