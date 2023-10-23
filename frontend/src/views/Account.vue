<template>
  <v-container class="mt-8">
    <h1>Личный кабинет</h1>
    <v-container v-if="!isAuth">
      <h2>Вы не авторизованы</h2>
    </v-container>
    <v-container v-if="isAuth">
      <h2>Вы авторизованы</h2>

      <p>Имя пользователя: {{accountData.username}}</p>
      <p>Email: {{accountData.email}}</p>

      <router-link to="logout" v-slot="{href, isExactActive, navigate}">
        <v-btn @click="navigate" :href="href" class="black--text mx-1" depressed>
          Выйти
        </v-btn>
      </router-link>
    </v-container>
  </v-container>
</template>

<script>
import router from "../router";
import axios from "axios";

export default {
  name: "Account",
  data() {
    return {
      isAuth: false,
      accountData: ''
    }
  },
  mounted() {
    this.isAuth = localStorage.getItem('auth-token');
    if (!this.isAuth) {
      return router.push('/login')
    }
    axios.get('http://127.0.0.1:8000/auth/users/me', {
      headers: {
        Authorization: `Token ${this.isAuth}`
      }
    }).then(res => {
      this.accountData = res.data;
    }).catch((err) => {
      console.log(err)
    })
  }
}
</script>

<style scoped>

</style>
