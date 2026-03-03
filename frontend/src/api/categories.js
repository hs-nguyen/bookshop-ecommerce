import apiClient from './client';

export default {
  getCategories() {
    return apiClient.get('/categories/');
  },
  getCategoryBooks(id) {
    return apiClient.get(`/categories/${id}/books/`);
  },
};