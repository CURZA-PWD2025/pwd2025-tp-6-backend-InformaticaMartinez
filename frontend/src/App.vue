<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
  <div class="app-container">
    <header>
      <h1>Administrador de Archivos</h1>
      <nav>
        <RouterLink to="/marcas">Marcas</RouterLink>
        <RouterLink to="/categorias">Categorías</RouterLink>
        <RouterLink to="/articulos">Artículos</RouterLink>
        <RouterLink to="/proveedores">Proveedores</RouterLink>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-container {
  text-align: center,top;
  padding: 2rem;
  color: #ddd;
  font-family: 'Segoe UI', sans-serif;
}

header h1 {
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #eee;
}

nav {
  display: flex;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

nav a {
  color: #00e0aa;
  text-decoration: none;
  font-weight: bold;
  background-color: #222;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: background-color 0.3s;
}

nav a:hover {
  background-color: #333;
  color: #ffffff;
}

main {
  max-width: 900px;
  margin: 0 auto;
}
</style>
