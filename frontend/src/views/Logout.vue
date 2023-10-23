<template>
  <h1>Выходим из системы..</h1>
</template>

<script>
import router from "../router";

export default {
  name: "Logout",
  mounted() {
    this.isAuth = localStorage.getItem('auth-token');
    if (!this.isAuth) {
      return router.push('/login')
    }

    localStorage.removeItem('auth-token');
    router.push('/')
  }
}
</script>

<style scoped>

</style>
