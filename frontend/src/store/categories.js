import { defineStore } from 'pinia';
import categoriesApi from '../api/categories';

export const useCategoriesStore = defineStore('categories', {
  state: () => ({
    categories: [],
    selectedCategory: null,
  }),
  actions: {
    async fetchCategories() {
      const response = await categoriesApi.getCategories();
      this.categories = response.data.results || response.data;
    },
  },
});