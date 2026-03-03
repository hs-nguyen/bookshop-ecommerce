<template>
  <div class="category-filter">
    <h3>Categories</h3>
    <div class="filter-buttons">
      <button @click="selectCategory(null)" :class="{ active: !selectedCategory }">All Books</button>
      <button v-for="cat in categoriesStore.categories" :key="cat.id" 
              @click="selectCategory(cat.id)" 
              :class="{ active: selectedCategory === cat.id }">
        {{ cat.name }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCategoriesStore } from '../store/categories';

const emit = defineEmits(['category-selected']);
const categoriesStore = useCategoriesStore();
const selectedCategory = ref(null);

onMounted(() => {
  categoriesStore.fetchCategories();
});

const selectCategory = (id) => {
  selectedCategory.value = id;
  emit('category-selected', id);
};
</script>

<style scoped>
.category-filter {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}
h3 {
  margin: 0 0 1rem 0;
  color: #2c3e50;
}
.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
button {
  padding: 10px 20px;
  border: 2px solid #ddd;
  background: white;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.95rem;
}
button:hover {
  border-color: #3498db;
  color: #3498db;
}
button.active {
  background: #3498db;
  color: white;
  border-color: #3498db;
}
</style>