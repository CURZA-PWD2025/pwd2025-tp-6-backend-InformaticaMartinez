import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default {
  async getAll(endpoint: string) {
    const res = await api.get(endpoint);
    return res.data;
  },
  async getOne(endpoint: string, id: number) {
    const res = await api.get(`${endpoint}/${id}`);
    return res.data;
  },
  async create(endpoint: string, data: any) {
    const res = await api.post(endpoint, data);
    return res.data;
  },
  async update(endpoint: string, id: number, data: any) {
    const res = await api.put(`${endpoint}/${id}`, data);
    return res.data;
  },
  async destroy(endpoint: string, id: number) {
    const res = await api.delete(`${endpoint}/${id}`);
    return res.data;
  }
};
