<template>
  <header>
    <nav>
      <router-link to="/">Bookshop</router-link>
      <div v-if="authStore.isAuthenticated">
        <span>{{ authStore.user?.username }}</span>
        <CartIcon />
        <router-link to="/orders">Orders</router-link>
        <router-link to="/profile">Profile</router-link>
        <button @click="logout">Logout</button>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { useAuthStore } from '../store/auth';
import CartIcon from './CartIcon.vue';

const authStore = useAuthStore();

const logout = () => {
  authStore.logout();
};
</script>

<style scoped>
header { background: #333; color: white; padding: 1rem; }
nav { display: flex; justify-content: space-between; align-items: center; }
a { color: white; margin: 0 10px; text-decoration: none; }
button { background: #555; color: white; border: none; padding: 5px 10px; cursor: pointer; }
</style>