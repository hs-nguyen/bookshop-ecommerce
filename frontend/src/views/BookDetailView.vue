<template>
  <div class="book-detail" v-if="booksStore.currentBook">
    <div class="book-container">
      <div class="book-image">
        <img :src="booksStore.currentBook.image_url" :alt="booksStore.currentBook.title" />
      </div>
      <div class="book-info">
        <h1>{{ booksStore.currentBook.title }}</h1>
        <p class="author">by {{ booksStore.currentBook.author }}</p>
        <p class="category" v-if="booksStore.currentBook.category_name">
          {{ booksStore.currentBook.category_name }}
        </p>
        <p class="price">${{ booksStore.currentBook.price }}</p>
        <p class="stock" :class="stockClass">{{ stockText }}</p>
        <p class="description">{{ booksStore.currentBook.description }}</p>
        <div class="actions">
          <input v-model.number="quantity" type="number" min="1" :max="booksStore.currentBook.stock_quantity" />
          <button @click="addToCart" :disabled="booksStore.currentBook.stock_quantity === 0">
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  </div>
  <div v-else class="loading">Loading...</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useBooksStore } from '../store/books';
import { useCartStore } from '../store/cart';

const route = useRoute();
const router = useRouter();
const booksStore = useBooksStore();
const cartStore = useCartStore();
const quantity = ref(1);

const stockClass = computed(() => {
  const stock = booksStore.currentBook?.stock_quantity || 0;
  if (stock === 0) return 'out-of-stock';
  if (stock < 5) return 'low-stock';
  return 'in-stock';
});

const stockText = computed(() => {
  const stock = booksStore.currentBook?.stock_quantity || 0;
  if (stock === 0) return 'Out of Stock';
  if (stock < 5) return `Only ${stock} left`;
  return `In Stock (${stock})`;
});

const addToCart = async () => {
  try {
    await cartStore.addToCart(booksStore.currentBook.id, quantity.value);
    router.push('/cart');
  } catch (error) {
    alert('Failed to add to cart');
  }
};

onMounted(() => {
  booksStore.fetchBook(route.params.id);
});
</script>

<style scoped>
.book-detail {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
}
.book-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}
.book-image img {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.book-info h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.author {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1rem;
}
.category {
  display: inline-block;
  background: #f0f0f0;
  padding: 6px 12px;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}
.price {
  font-size: 2rem;
  font-weight: bold;
  color: #2c3e50;
  margin: 1rem 0;
}
.stock {
  font-size: 1rem;
  font-weight: 500;
  margin-bottom: 1rem;
}
.in-stock { color: #27ae60; }
.low-stock { color: #f39c12; }
.out-of-stock { color: #e74c3c; }
.description {
  line-height: 1.6;
  color: #555;
  margin: 1.5rem 0;
}
.actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;
}
input {
  width: 80px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}
button {
  flex: 1;
  padding: 12px 24px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}
button:hover:not(:disabled) {
  background: #2980b9;
}
button:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}
.loading {
  text-align: center;
  padding: 3rem;
  font-size: 1.2rem;
  color: #666;
}
@media (max-width: 768px) {
  .book-container {
    grid-template-columns: 1fr;
  }
}
</style>
