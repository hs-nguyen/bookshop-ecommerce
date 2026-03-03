<template>
  <div class="order-detail" v-if="ordersStore.currentOrder">
    <div class="order-header">
      <h1>Order #{{ ordersStore.currentOrder.id }}</h1>
      <span class="status" :class="ordersStore.currentOrder.status">
        {{ ordersStore.currentOrder.status }}
      </span>
    </div>
    
    <div class="order-info">
      <div class="info-card">
        <h3>Order Information</h3>
        <p><strong>Order Date:</strong> {{ formatDate(ordersStore.currentOrder.order_date) }}</p>
        <p><strong>Status:</strong> {{ ordersStore.currentOrder.status }}</p>
        <p><strong>Total Amount:</strong> ${{ ordersStore.currentOrder.total_price }}</p>
      </div>
    </div>

    <div class="order-items">
      <h3>Order Items</h3>
      <div v-for="item in ordersStore.currentOrder.items" :key="item.id" class="item-card">
        <img :src="item.book_details.image_url" :alt="item.book_details.title" />
        <div class="item-info">
          <h4>{{ item.book_details.title }}</h4>
          <p class="author">by {{ item.book_details.author }}</p>
          <p class="quantity">Quantity: {{ item.quantity }}</p>
          <p class="price">${{ item.price_at_purchase }} each</p>
        </div>
        <div class="item-total">
          <p>${{ (item.quantity * item.price_at_purchase).toFixed(2) }}</p>
        </div>
      </div>
    </div>

    <div class="order-summary">
      <h3>Order Summary</h3>
      <div class="summary-row">
        <span>Subtotal:</span>
        <span>${{ ordersStore.currentOrder.total_price }}</span>
      </div>
      <div class="summary-row total">
        <span>Total:</span>
        <span>${{ ordersStore.currentOrder.total_price }}</span>
      </div>
    </div>

    <div class="actions">
      <router-link to="/orders" class="btn-secondary">Back to Orders</router-link>
      <router-link to="/" class="btn-primary">Continue Shopping</router-link>
    </div>
  </div>
  <div v-else class="loading">Loading order details...</div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useOrdersStore } from '../store/orders';

const route = useRoute();
const ordersStore = useOrdersStore();

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  });
};

onMounted(() => {
  ordersStore.fetchOrder(route.params.id);
});
</script>

<style scoped>
.order-detail {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 2rem;
}
.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 2px solid #eee;
}
.order-header h1 {
  margin: 0;
  color: #2c3e50;
}
.status {
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  text-transform: capitalize;
}
.status.pending { background: #fff3cd; color: #856404; }
.status.confirmed { background: #d1ecf1; color: #0c5460; }
.status.shipped { background: #d4edda; color: #155724; }
.status.delivered { background: #d4edda; color: #155724; }
.status.cancelled { background: #f8d7da; color: #721c24; }
.order-info {
  margin-bottom: 2rem;
}
.info-card {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
}
.info-card h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2c3e50;
}
.info-card p {
  margin: 0.5rem 0;
  color: #555;
}
.order-items {
  margin-bottom: 2rem;
}
.order-items h3 {
  margin-bottom: 1rem;
  color: #2c3e50;
}
.item-card {
  display: grid;
  grid-template-columns: 100px 1fr auto;
  gap: 1.5rem;
  padding: 1.5rem;
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 1rem;
}
.item-card img {
  width: 100px;
  height: 140px;
  object-fit: cover;
  border-radius: 4px;
}
.item-info h4 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
}
.author {
  color: #666;
  font-size: 0.9rem;
  margin: 0.25rem 0;
}
.quantity, .price {
  margin: 0.5rem 0;
  color: #555;
}
.item-total {
  text-align: right;
  font-size: 1.2rem;
  font-weight: bold;
  color: #2c3e50;
}
.order-summary {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}
.order-summary h3 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #2c3e50;
}
.summary-row {
  display: flex;
  justify-content: space-between;
  padding: 0.5rem 0;
  color: #555;
}
.summary-row.total {
  border-top: 2px solid #ddd;
  margin-top: 0.5rem;
  padding-top: 1rem;
  font-size: 1.3rem;
  font-weight: bold;
  color: #2c3e50;
}
.actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
}
.btn-primary, .btn-secondary {
  padding: 12px 24px;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 500;
}
.btn-primary {
  background: #3498db;
  color: white;
}
.btn-secondary {
  background: white;
  color: #3498db;
  border: 2px solid #3498db;
}
.btn-primary:hover {
  background: #2980b9;
}
.btn-secondary:hover {
  background: #f8f9fa;
}
.loading {
  text-align: center;
  padding: 3rem;
  font-size: 1.2rem;
  color: #666;
}
@media (max-width: 768px) {
  .item-card {
    grid-template-columns: 80px 1fr;
  }
  .item-total {
    grid-column: 2;
    text-align: left;
    margin-top: 0.5rem;
  }
}
</style>
