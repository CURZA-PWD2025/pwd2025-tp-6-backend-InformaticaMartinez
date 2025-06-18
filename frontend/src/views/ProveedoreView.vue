<template>
  <div>
    <h1>Gestión de Proveedores</h1>
    <ProveedorForm />
    <ProveedorList />
  </div>
</template>

<script setup lang="ts">
import ProveedorForm from '@/components/proveedores/ProveedorForm.vue';
import ProveedorList from '@/components/proveedores/ProveedorList.vue';
</script>