import { defineStore } from 'pinia';
import cartApi from '../api/cart';

export const useCartStore = defineStore('cart', {
  state: () => ({
    items: [],
  }),
  getters: {
    itemCount: (state) => state.items.reduce((sum, item) => sum + item.quantity, 0),
    totalPrice: (state) => state.items.reduce((sum, item) => sum + item.subtotal, 0),
  },
  actions: {
    async fetchCart() {
      const response = await cartApi.getCart();
      this.items = response.data;
    },
    async addToCart(bookId, quantity = 1) {
      await cartApi.addToCart({ book: bookId, quantity });
      await this.fetchCart();
    },
    async updateQuantity(itemId, quantity) {
      await cartApi.updateCartItem(itemId, { quantity });
      await this.fetchCart();
    },
    async removeItem(itemId) {
      await cartApi.removeFromCart(itemId);
      await this.fetchCart();
    },
    async clearCart() {
      await cartApi.clearCart();
      this.items = [];
    },
  },
});