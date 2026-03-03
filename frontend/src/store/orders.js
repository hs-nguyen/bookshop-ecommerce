import { defineStore } from 'pinia';
import ordersApi from '../api/order';

export const useOrdersStore = defineStore('orders', {
  state: () => ({
    orders: [],
    currentOrder: null,
  }),
  actions: {
    async createOrder() {
      const response = await ordersApi.createOrder();
      this.currentOrder = response.data;
      return response.data;
    },
    async fetchOrders() {
      const response = await ordersApi.getOrders();
      this.orders = response.data.results || response.data;
    },
    async fetchOrder(id) {
      const response = await ordersApi.getOrder(id);
      this.currentOrder = response.data;
    },
  },
});