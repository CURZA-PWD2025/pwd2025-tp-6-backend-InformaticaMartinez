<template>
  <form @submit.prevent="onSubmit" class="formulario">
    <h2>Crear Marca</h2>
    <input v-model="nombre" placeholder="Nombre de la marca" class="input" />
    <button type="submit" class="boton">Agregar Marca</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useMarcaStore } from '@/stores/marcaStore';

const store = useMarcaStore();
const nombre = ref('');

const onSubmit = async () => {
  await store.create({ nombre: nombre.value });
  nombre.value = '';
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

.formulario h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: #333;
}

.input,
select {
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