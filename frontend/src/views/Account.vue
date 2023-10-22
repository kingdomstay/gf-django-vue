<template>
  <v-container class="mt-8">
    <h1>Личный кабинет</h1>
    <v-container v-if="!isAuth">
      <h2>Вы не авторизованы</h2>
    </v-container>
    <v-container v-if="isAuth">
      <h2>Вы авторизованы</h2>
    </v-container>
  </v-container>
</template>

<script>
import router from "../router";

export default {
  name: "Account",
  data() {
    return {
      isAuth: false
    }
  },
  mounted() {
    const authToken = localStorage.getItem('auth-token');
    if (!authToken) {
      router.push('/login')
    }
  }
export default {
  name: "Account"
}
</script>

<style scoped>

</style>
