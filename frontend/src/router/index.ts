import { createRouter, createWebHistory } from 'vue-router';
import ProveedoreView from '@/views/ProveedoreView.vue';
import MarcasView from '@/views/MarcasView.vue';
import CategoriasView from '@/views/CategoriasView.vue';
import ArticulosView from '@/views/ArticulosView.vue';

const routes = [
  { path: '/marcas', name: 'marcas', component: MarcasView },
  { path: '/categorias', name: 'categorias', component: CategoriasView },
  { path: '/articulos', name: 'articulos', component: ArticulosView },
  { path: '/proveedores', name: 'proveedores', component: ProveedoreView },
];


export default createRouter({
  history: createWebHistory(),
  routes,
});