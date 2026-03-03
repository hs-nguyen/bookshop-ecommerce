import apiClient from './client';

export default {
  getCart() {
    return apiClient.get('/cart/');
  },
  addToCart(data) {
    return apiClient.post('/cart/', data);
  },
  updateCartItem(id, data) {
    return apiClient.put(`/cart/${id}/`, data);
  },
  removeFromCart(id) {
    return apiClient.delete(`/cart/${id}/`);
  },
  clearCart() {
    return apiClient.delete('/cart/clear/');
  },
};