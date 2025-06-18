<template>
  <form @submit.prevent="onSubmit" class="formulario">
    <h2>{{ isEdit ? 'Editar Artículo' : 'Crear Artículo' }}</h2>
    <input v-model="articulo.descripcion" placeholder="Descripción" class="input" />
    <input v-model="articulo.precio" placeholder="Precio" class="input" />
    <input v-model="articulo.stock" placeholder="Stock" class="input" />

    <select v-model.number="articulo.marca_id" class="input">
      <option disabled value="0">Seleccione Marca</option>
      <option v-for="m in marcas" :key="m.id" :value="m.id">{{ m.nombre }}</option>
    </select>

    <select v-model.number="articulo.proveedor_id" class="input">
      <option disabled value="0">Seleccione Proveedor</option>
      <option v-for="p in proveedores" :key="p.id" :value="p.id">{{ p.nombre }}</option>
    </select>

    <div class="checkboxes">
      <label v-for="c in categorias" :key="c.id">
        <input type="checkbox" :value="c.id" v-model="articulo.categorias" /> {{ c.nombre }}
      </label>
    </div>

    <button type="submit" class="boton">{{ isEdit ? 'Actualizar' : 'Crear' }}</button>
  </form>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useArticuloStore } from '@/stores/articuloStore';
import { useMarcaStore } from '@/stores/marcaStore';
import { useCategoriaStore } from '@/stores/categoriaStore';
import ApiService from '@/services/ApiService';

const articuloStore = useArticuloStore();
const marcaStore = useMarcaStore();
const categoriaStore = useCategoriaStore();

const marcas = ref([] as any[]);
const categorias = ref([] as any[]);
const proveedores = ref([] as any[]);

const articulo = ref({
  descripcion: '',
  precio: '',
  stock: '',
  marca_id: 0,
  proveedor_id: 0,
  categorias: [] as number[],
});

const isEdit = ref(false);
const editId = ref<number | null>(null);

const onSubmit = async () => {
  const data = {
    descripcion: articulo.value.descripcion,
    precio: articulo.value.precio,
    stock: articulo.value.stock,
    marca_id: articulo.value.marca_id,
    proveedor_id: articulo.value.proveedor_id,
    categorias: articulo.value.categorias.map(id => ({ id })),
  };

  if (isEdit.value && editId.value !== null) {
    await articuloStore.update(editId.value, data);
  } else {
    await articuloStore.create(data);
  }
  resetForm();
};

const resetForm = () => {
  articulo.value = {
    descripcion: '',
    precio: '',
    stock: '',
    marca_id: 0,
    proveedor_id: 0,
    categorias: [],
  };
  isEdit.value = false;
  editId.value = null;
};

onMounted(async () => {
  await marcaStore.fetch();
  await categoriaStore.fetch();
  marcas.value = marcaStore.marcas;
  categorias.value = categoriaStore.categorias;
  proveedores.value = await ApiService.getAll('/proveedores');
});
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

.checkboxes label {
  display: inline-block;
  margin: 0.5rem 1rem 0.5rem 0;
  color: #333;
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