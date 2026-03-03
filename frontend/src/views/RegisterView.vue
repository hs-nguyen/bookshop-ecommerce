<template>
  <div class="register-form">
    <h1>Register</h1>
    <form @submit.prevent="handleRegister">
      <input v-model="username" placeholder="Username" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <input v-model="password2" type="password" placeholder="Confirm Password" required />
      <button type="submit">Register</button>
      <p v-if="error">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../store/auth';

const router = useRouter();
const authStore = useAuthStore();
const username = ref('');
const email = ref('');
const password = ref('');
const password2 = ref('');
const error = ref('');

const handleRegister = async () => {
  if (password.value !== password2.value) {
    error.value = 'Passwords do not match';
    return;
  }
  try {
    await authStore.register({ username: username.value, email: email.value, password: password.value, password2: password2.value });
    router.push('/login');
  } catch (err) {
    error.value = 'Registration failed';
  }
};
</script>

<style scoped>
.register-form { max-width: 400px; margin: 50px auto; }
input { display: block; width: 100%; padding: 10px; margin: 10px 0; }
button { width: 100%; padding: 10px; cursor: pointer; }
</style>