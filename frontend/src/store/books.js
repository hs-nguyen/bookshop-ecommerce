import { defineStore } from 'pinia';
import booksApi from '../api/books';

export const useBooksStore = defineStore('books', {
  state: () => ({
    books: [],
    currentBook: null,
    loading: false,
  }),
  actions: {
    async fetchBooks(categoryId = null) {
      this.loading = true;
      const response = await booksApi.getBooks(categoryId);
      this.books = response.data.results || response.data;
      this.loading = false;
    },
    async fetchBook(id) {
      this.loading = true;
      const response = await booksApi.getBook(id);
      this.currentBook = response.data;
      this.loading = false;
    },
  },
});