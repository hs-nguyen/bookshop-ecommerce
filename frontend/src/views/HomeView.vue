<template>
  <div class="home">
    <div class="hero">
      <h1>Welcome to Bookshop</h1>
      <p>Discover your next favorite book</p>
    </div>
    
    <CategoryFilter @category-selected="filterByCategory" />
    
    <div v-if="booksStore.loading" class="loading">Loading books...</div>
    <div v-else-if="booksStore.books.length === 0" class="no-books">No books found</div>
    <div v-else class="book-grid">
      <BookCard v-for="book in booksStore.books" :key="book.id" :book="book" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useBooksStore } from '../store/books';
import BookCard from '../components/BookCard.vue';
import CategoryFilter from '../components/CategoryFilter.vue';

const booksStore = useBooksStore();

onMounted(() => {
  booksStore.fetchBooks();
});

const filterByCategory = (categoryId) => {
  booksStore.fetchBooks(categoryId);
};
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}
.hero {
  text-align: center;
  padding: 3rem 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 12px;
  margin-bottom: 2rem;
}
.hero h1 {
  font-size: 2.5rem;
  margin: 0 0 1rem 0;
}
.hero p {
  font-size: 1.2rem;
  opacity: 0.9;
}
.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 24px;
}
.loading, .no-books {
  text-align: center;
  padding: 3rem;
  color: #666;
  font-size: 1.1rem;
}
</style>