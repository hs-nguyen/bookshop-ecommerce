<template>
  <div>
    <h1>Shopping Cart</h1>
    <div v-if="cartStore.items.length === 0">Your cart is empty</div>
    <div v-else>
      <div v-for="item in cartStore.items" :key="item.id" class="cart-item">
        <h3>{{ item.book_details.title }}</h3>
        <p>${{ item.book_details.price }} x {{ item.quantity }}</p>
        <button @click="cartStore.updateQuantity(item.id, item.quantity - 1)" :disabled="item.quantity <= 1">-</button>
        <span>{{ item.quantity }}</span>
        <button @click="cartStore.updateQuantity(item.id, item.quantity + 1)">+</button>
        <button @click="cartStore.removeItem(item.id)">Remove</button>
      </div>
      <h2>Total: ${{ cartStore.totalPrice }}</h2>
      <button @click="checkout">Checkout</button>
      <button @click="cartStore.clearCart()">Clear Cart</button>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useCartStore } from '../store/cart';
import { useOrdersStore } from '../store/orders';

const router = useRouter();
const cartStore = useCartStore();
const ordersStore = useOrdersStore();

onMounted(() => {
  cartStore.fetchCart();
});

const checkout = async () => {
  try {
    const order = await ordersStore.createOrder();
    await cartStore.fetchCart();
    router.push(`/orders/${order.id}`);
  } catch (error) {
    alert(error.response?.data?.error || 'Checkout failed');
  }
};
</script>

<style scoped>
.cart-item { border: 1px solid #ddd; padding: 1rem; margin: 10px 0; }
button { margin: 5px; padding: 8px 16px; cursor: pointer; }
</style>