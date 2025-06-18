import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';

export const useMarcaStore = defineStore('marca', {
  state: () => ({ marcas: [] as any[] }),
  actions: {
    async fetch() {
      this.marcas = await ApiService.getAll('/marcas');
    },
    async create(data: any) {
      await ApiService.create('/marcas', data);
      await this.fetch();
    },
    async update(id: number, data: any) {
      await ApiService.update('/marcas', id, data);
      await this.fetch();
    },
    async destroy(id: number) {
      await ApiService.destroy('/marcas', id);
      await this.fetch();
    },
  },
});