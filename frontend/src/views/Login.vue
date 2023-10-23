<template>
  <v-container>
    <v-sheet max-width="450" class="mx-auto">
      <h1 class="my-4">Авторизация</h1>
      <v-form v-model="valid" @submit.prevent="submit">
        <v-text-field
            label="Имя пользователя"
            required
            hide-details
            :rules="rules"
            v-model="username"
        ></v-text-field>
        <v-text-field
            type="password"
            label="Пароль"
            :rules="rules"
            v-model="password"
        ></v-text-field>

        <v-btn :disabled="!valid" type="submit" block class="mt-2">Войти</v-btn>

        <p class="my-2 red--text" v-if="error">{{error}}</p>
      </v-form>
    </v-sheet>
  </v-container>
</template>

<script>
import axios from "axios";
import router from "../router";

export default {
  name: "Login",
  data: () => ({
    valid: false,
    username: '',
    password: '',
    error: '',
    rules: [
      value => {
        if (value) return true

        return 'Введите корректные данные'
      },
    ]
  }),
  methods: {
    async submit () {
      this.error = '';
      axios.postForm('http://127.0.0.1:8000/auth/token/login/', {
        username: this.username,
        password: this.password
      }).then(res => {
        localStorage.setItem('auth-token', res.data.auth_token);
        router.push('/account');
      }).catch(err => {
        this.error = `Ошибка: ${err.response.data.non_field_errors[0]}`;
      });
    },
  },
  mounted() {
    const authToken = localStorage.getItem('auth-token');
    if (authToken) {
      router.push('/account')
    }
  }
}
</script>

<style scoped>

</style>
