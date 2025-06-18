import { defineStore } from 'pinia';
import ApiService from '@/services/ApiService';

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({ proveedores: [] as any[] }),
  actions: {
    async fetch() {
      this.proveedores = await ApiService.getAll('/proveedores');
    },
    async create(data: any) {
      await ApiService.create('/proveedores', data);
      await this.fetch();
    },
    async update(id: number, data: any) {
      await ApiService.update('/proveedores', id, data);
      await this.fetch();
    },
    async destroy(id: number) {
      await ApiService.destroy('/proveedores', id);
      await this.fetch();
    },
  },
});