import apiClient from './client';

export default {
  getBooks(categoryId = null) {
    const params = categoryId ? { category: categoryId } : {};
    return apiClient.get('/books/', { params });
  },
  getBook(id) {
    return apiClient.get(`/books/${id}/`);
  },
};