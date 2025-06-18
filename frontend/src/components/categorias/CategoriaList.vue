<template>
  <div class="listado">
    <h2>Listado de Categorías</h2>
    <ul class="articulo-list">
      <li v-for="c in store.categorias" :key="c.id" class="item">
        {{ c.nombre }}
        <button @click="store.destroy(c.id)" class="boton-eliminar">Eliminar</button>
      </li>
    </ul>
  </div>
</template>
<script setup lang="ts">
import { onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';

const store = useCategoriaStore();
onMounted(() => store.fetch());
</script>
<style scoped>
.listado {
  max-width: 700px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #504e4e;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  color: #000;
}

.articulo-list {
  list-style: none;
  padding: 0;
}

.item {
  background: #9b9999;
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 1rem;
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.boton-eliminar {
  background-color: crimson;
  color: #222;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.boton-eliminar:hover {
  background-color: darkred;
}
</style>
