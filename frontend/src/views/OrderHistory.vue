<template>
  <div class="order-history">
    <h1>Order History</h1>
    <div v-if="ordersStore.orders.length === 0" class="no-orders">
      <p>You haven't placed any orders yet.</p>
      <router-link to="/" class="btn">Start Shopping</router-link>
    </div>
    <div v-else class="orders-list">
      <div v-for="order in ordersStore.orders" :key="order.id" class="order-card">
        <div class="order-header">
          <h3>Order #{{ order.id }}</h3>
          <span class="status" :class="order.status">{{ order.status }}</span>
        </div>
        <div class="order-details">
          <p><strong>Date:</strong> {{ formatDate(order.order_date) }}</p>
          <p><strong>Total:</strong> ${{ order.total_price }}</p>
          <p><strong>Items:</strong> {{ order.items?.length || 0 }}</p>
        </div>
        <router-link :to="`/orders/${order.id}`" class="view-btn">View Details</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useOrdersStore } from '../store/orders';

const ordersStore = useOrdersStore();

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};

onMounted(() => {
  ordersStore.fetchOrders();
});
</script>

<style scoped>
.order-history {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 2rem;
}
h1 {
  margin-bottom: 2rem;
  color: #2c3e50;
}
.no-orders {
  text-align: center;
  padding: 3rem;
  background: #f8f9fa;
  border-radius: 8px;
}
.no-orders p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1.5rem;
}
.btn {
  display: inline-block;
  padding: 12px 24px;
  background: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}
.orders-list {
  display: grid;
  gap: 1.5rem;
}
.order-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.order-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid #eee;
}
.order-header h3 {
  margin: 0;
  color: #2c3e50;
}
.status {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  text-transform: capitalize;
}
.status.pending { background: #fff3cd; color: #856404; }
.status.confirmed { background: #d1ecf1; color: #0c5460; }
.status.shipped { background: #d4edda; color: #155724; }
.status.delivered { background: #d4edda; color: #155724; }
.status.cancelled { background: #f8d7da; color: #721c24; }
.order-details {
  margin: 1rem 0;
}
.order-details p {
  margin: 0.5rem 0;
  color: #555;
}
.view-btn {
  display: inline-block;
  margin-top: 1rem;
  padding: 8px 16px;
  background: #3498db;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  font-size: 0.9rem;
}
.view-btn:hover {
  background: #2980b9;
}
</style>
