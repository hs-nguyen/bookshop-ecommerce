<template>
  <router-link to="/cart" class="cart-icon">
    🛒 <span class="badge">{{ cartStore.itemCount }}</span>
  </router-link>
</template>

<script setup>
import { onMounted } from 'vue';
import { useCartStore } from '../store/cart';

const cartStore = useCartStore();

onMounted(() => {
  if (cartStore.itemCount === 0) {
    cartStore.fetchCart();
  }
});
</script>

<style scoped>
.cart-icon { position: relative; }
.badge { background: red; color: white; border-radius: 50%; padding: 2px 6px; font-size: 12px; }
</style>