<template>
  <div class="listado">
    <h2>Listado de Artículos</h2>
    <ul class="articulo-list">
      <li v-for="a in store.articulos" :key="a.id" class="item">
        <p><strong>{{ a.descripcion }}</strong></p>
        <p>Precio: ${{ a.precio }} | Stock: {{ a.stock }}</p>
        <p>Marca: {{ a.marca_id }} | Proveedor: {{ a.proveedor_id }}</p>
        <p>
          Categorías:
          <span v-if="a.categorias && Array.isArray(a.categorias)">
            {{ a.categorias.map(c => c.nombre).join(', ') }}
          </span>
          <span v-else>
            Sin categorías
          </span>
        </p>
        <button @click="store.destroy(a.id)" class="boton-eliminar">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useArticuloStore } from '@/stores/articuloStore';

const store = useArticuloStore();
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
}

.boton-eliminar {
  background-color: crimson;
  position: top left;
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
