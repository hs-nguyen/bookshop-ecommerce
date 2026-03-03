import apiClient from './client';

export default {
  register(data) {
    return apiClient.post('/auth/register/', data);
  },
  login(data) {
    return apiClient.post('/auth/login/', data);
  },
  getProfile() {
    return apiClient.get('/auth/profile/');
  },
  updateProfile(data) {
    return apiClient.put('/auth/profile/', data);
  },
  deleteAccount() {
    return apiClient.delete('/auth/profile/');
  },
};