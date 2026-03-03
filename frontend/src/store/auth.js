import { defineStore } from 'pinia';
import authApi from '../api/auth';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: sessionStorage.getItem('token'),
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
  },
  actions: {
    async login(credentials) {
      const response = await authApi.login(credentials);
      this.token = response.data.access;
      sessionStorage.setItem('token', this.token);
      await this.fetchProfile();
    },
    async register(data) {
      await authApi.register(data);
    },
    async fetchProfile() {
      const response = await authApi.getProfile();
      this.user = response.data;
    },
    logout() {
      this.user = null;
      this.token = null;
      sessionStorage.removeItem('token');
    },
  },
});