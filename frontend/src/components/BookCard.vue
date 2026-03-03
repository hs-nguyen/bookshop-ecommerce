<template>
  <div class="book-card" @click="goToDetail">
    <img :src="book.image_url" :alt="book.title" />
    <div class="book-info">
      <h3>{{ book.title }}</h3>
      <p class="author">by {{ book.author }}</p>
      <p class="category" v-if="book.category_name">{{ book.category_name }}</p>
      <p class="price">${{ book.price }}</p>
      <p class="stock" :class="stockClass">
        {{ stockText }}
      </p>
      <button @click.stop="addToCart" :disabled="book.stock_quantity === 0">Add to Cart</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useCartStore } from '../store/cart';

const props = defineProps(['book']);
const router = useRouter();
const cartStore = useCartStore();

const stockClass = computed(() => {
  if (props.book.stock_quantity === 0) return 'out-of-stock';
  if (props.book.stock_quantity < 5) return 'low-stock';
  return 'in-stock';
});

const stockText = computed(() => {
  if (props.book.stock_quantity === 0) return 'Out of Stock';
  if (props.book.stock_quantity < 5) return `Only ${props.book.stock_quantity} left`;
  return `In Stock (${props.book.stock_quantity})`;
});

const goToDetail = () => {
  router.push(`/books/${props.book.id}`);
};

const addToCart = async () => {
  await cartStore.addToCart(props.book.id);
};
</script>

<style scoped>
.book-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
  cursor: pointer;
}
.book-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
img {
  width: 100%;
  height: 250px;
  object-fit: cover;
}
.book-info {
  padding: 1rem;
}
h3 {
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
  color: #333;
}
.author {
  color: #666;
  font-size: 0.9rem;
  margin: 0 0 0.5rem 0;
}
.category {
  display: inline-block;
  background: #f0f0f0;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
  color: #555;
  margin-bottom: 0.5rem;
}
.price {
  font-size: 1.3rem;
  font-weight: bold;
  color: #2c3e50;
  margin: 0.5rem 0;
}
.stock {
  font-size: 0.9rem;
  margin: 0.5rem 0;
  font-weight: 500;
}
.in-stock { color: #27ae60; }
.low-stock { color: #f39c12; }
.out-of-stock { color: #e74c3c; }
button {
  width: 100%;
  margin-top: 10px;
  padding: 10px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background 0.2s;
}
button:hover:not(:disabled) {
  background: #2980b9;
}
button:disabled {
  background: #bdc3c7;
  cursor: not-allowed;
}
</style>