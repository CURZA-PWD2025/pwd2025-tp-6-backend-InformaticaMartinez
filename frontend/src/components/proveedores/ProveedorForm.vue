<template>
  <form @submit.prevent="onSubmit" class="formulario">
    <h2>Crear Proveedor</h2>
    <input v-model="proveedor.nombre" placeholder="Nombre" class="input" />
    <input v-model="proveedor.telefono" placeholder="Teléfono" class="input" />
    <input v-model="proveedor.direccion" placeholder="Dirección" class="input" />
    <input v-model="proveedor.email" placeholder="Email" class="input" />
    <button type="submit" class="boton">Crear</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useProveedorStore } from '@/stores/proveedorStore';

const store = useProveedorStore();

const proveedor = ref({
  nombre: '',
  telefono: '',
  direccion: '',
  email: '',
});

const onSubmit = async () => {
  await store.create(proveedor.value);
  proveedor.value = {
    nombre: '',
    telefono: '',
    direccion: '',
    email: '',
  };
};
</script>

<style scoped>
.formulario {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #9b9999;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  color: #000;
}

.input {
  display: block;
  width: 100%;
  padding: 0.6rem;
  margin-bottom: 1rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #000;
}

.boton {
  background-color: #00e0aa;
  color: #222;
  padding: 0.6rem 1.2rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}
.boton:hover {
  background-color: #056e5d;
}
</style>
