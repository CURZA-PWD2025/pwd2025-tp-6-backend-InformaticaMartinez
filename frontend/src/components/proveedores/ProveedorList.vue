<template>
  <div class="listado">
    <h2>Listado de Proveedores</h2>
    <ul class="proveedor-list">
      <li v-for="p in store.proveedores" :key="p.id" class="item">
        <p><strong>{{ p.nombre }}</strong></p>
        <p>Teléfono: {{ p.telefono }}</p>
        <p>Dirección: {{ p.direccion }}</p>
        <p>Email: {{ p.email }}</p>
        <button @click="store.destroy(p.id)" class="boton-eliminar">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useProveedorStore } from '@/stores/proveedorStore';

const store = useProveedorStore();
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

.proveedor-list {
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
