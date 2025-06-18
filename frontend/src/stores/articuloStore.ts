import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';

interface Categoria {
  id: number;
  nombre: string;
}

interface Articulo {
  id: number;
  descripcion: string;
  precio: number;
  stock: number;
  marca_id: number;
  proveedor_id: number;
  categorias: Categoria[];
}

export const useArticuloStore = defineStore('articulo', {
  state: () => ({ articulos: [] as any[] }),
  actions: {
    async fetch() {
      this.articulos = await ApiService.getAll('/articulos');
    },
    async create(data: any) {
      await ApiService.create('/articulos', data);
      await this.fetch();
    },
    async update(id: number, data: any) {
      await ApiService.update('/articulos', id, data);
      await this.fetch();
    },
    async destroy(id: number) {
      await ApiService.destroy('/articulos', id);
      await this.fetch();
    },
  },
});
