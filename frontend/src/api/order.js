import apiClient from './client';

export default {
  createOrder() {
    return apiClient.post('/orders/');
  },
  getOrders() {
    return apiClient.get('/orders/');
  },
  getOrder(id) {
    return apiClient.get(`/orders/${id}/`);
  },
};