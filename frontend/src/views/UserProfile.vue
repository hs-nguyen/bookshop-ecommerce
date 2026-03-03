<template>
  <div class="user-profile">
    <h1>My Profile</h1>
    
    <div class="profile-card" v-if="authStore.user">
      <div class="profile-info">
        <h2>{{ authStore.user.username }}</h2>
        <p class="email">{{ authStore.user.email }}</p>
        <p class="member-since">Member since {{ formatDate(authStore.user.date_joined) }}</p>
      </div>

      <div class="profile-actions">
        <button @click="showEditForm = !showEditForm" class="btn-edit">
          {{ showEditForm ? 'Cancel' : 'Edit Profile' }}
        </button>
        <button @click="confirmDelete" class="btn-delete">Delete Account</button>
      </div>
    </div>

    <div v-if="showEditForm" class="edit-form">
      <h3>Edit Profile</h3>
      <form @submit.prevent="updateProfile">
        <div class="form-group">
          <label>Username</label>
          <input v-model="formData.username" type="text" required />
        </div>
        <div class="form-group">
          <label>Email</label>
          <input v-model="formData.email" type="email" required />
        </div>
        <button type="submit" class="btn-save">Save Changes</button>
        <p v-if="message" class="message" :class="messageType">{{ message }}</p>
      </form>
    </div>

    <div class="profile-stats">
      <h3>Account Statistics</h3>
      <div class="stats-grid">
        <div class="stat-card">
          <h4>{{ ordersStore.orders.length }}</h4>
          <p>Total Orders</p>
        </div>
        <div class="stat-card">
          <h4>{{ cartStore.itemCount }}</h4>
          <p>Items in Cart</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../store/auth';
import { useOrdersStore } from '../store/orders';
import { useCartStore } from '../store/cart';
import authApi from '../api/auth';

const router = useRouter();
const authStore = useAuthStore();
const ordersStore = useOrdersStore();
const cartStore = useCartStore();

const showEditForm = ref(false);
const message = ref('');
const messageType = ref('');
const formData = ref({
  username: '',
  email: ''
});

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  });
};

const updateProfile = async () => {
  try {
    await authApi.updateProfile(formData.value);
    await authStore.fetchProfile();
    message.value = 'Profile updated successfully!';
    messageType.value = 'success';
    showEditForm.value = false;
  } catch (error) {
    message.value = 'Failed to update profile';
    messageType.value = 'error';
  }
};

const confirmDelete = () => {
  if (confirm('Are you sure you want to delete your account? This action cannot be undone.')) {
    deleteAccount();
  }
};

const deleteAccount = async () => {
  try {
    await authApi.deleteAccount();
    authStore.logout();
    router.push('/');
  } catch (error) {
    alert('Failed to delete account');
  }
};

onMounted(async () => {
  if (authStore.user) {
    formData.value = {
      username: authStore.user.username,
      email: authStore.user.email
    };
  }
  await ordersStore.fetchOrders();
  await cartStore.fetchCart();
});
</script>

<style scoped>
.user-profile {
  max-width: 800px;
  margin: 2rem auto;
  padding: 2rem;
}
h1 {
  margin-bottom: 2rem;
  color: #2c3e50;
}
.profile-card {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 2rem;
  margin-bottom: 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.profile-info h2 {
  margin: 0 0 0.5rem 0;
  color: #2c3e50;
}
.email {
  color: #666;
  margin: 0.5rem 0;
}
.member-since {
  color: #999;
  font-size: 0.9rem;
  margin: 0.5rem 0;
}
.profile-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}
.btn-edit, .btn-delete {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.95rem;
}
.btn-edit {
  background: #3498db;
  color: white;
}
.btn-edit:hover {
  background: #2980b9;
}
.btn-delete {
  background: #e74c3c;
  color: white;
}
.btn-delete:hover {
  background: #c0392b;
}
.edit-form {
  background: #f8f9fa;
  padding: 2rem;
  border-radius: 8px;
  margin-bottom: 2rem;
}
.edit-form h3 {
  margin-top: 0;
  color: #2c3e50;
}
.form-group {
  margin-bottom: 1.5rem;
}
.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: #555;
  font-weight: 500;
}
.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}
.btn-save {
  padding: 12px 24px;
  background: #27ae60;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
}
.btn-save:hover {
  background: #229954;
}
.message {
  margin-top: 1rem;
  padding: 10px;
  border-radius: 4px;
}
.message.success {
  background: #d4edda;
  color: #155724;
}
.message.error {
  background: #f8d7da;
  color: #721c24;
}
.profile-stats {
  background: white;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 2rem;
}
.profile-stats h3 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  color: #2c3e50;
}
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1.5rem;
}
.stat-card {
  text-align: center;
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 8px;
}
.stat-card h4 {
  margin: 0;
  font-size: 2rem;
  color: #3498db;
}
.stat-card p {
  margin: 0.5rem 0 0 0;
  color: #666;
  font-size: 0.9rem;
}
</style>
