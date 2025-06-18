import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';

export const useCategoriaStore = defineStore('categoria', {
  state: () => ({ categorias: [] as any[] }),
  actions: {
    async fetch() {
      this.categorias = await ApiService.getAll('/categorias');
    },
    async create(data: any) {
      await ApiService.create('/categorias', data);
      await this.fetch();
    },
    async update(id: number, data: any) {
      await ApiService.update('/categorias', id, data);
      await this.fetch();
    },
    async destroy(id: number) {
      await ApiService.destroy('/categorias', id);
      await this.fetch();
    },
  },
});