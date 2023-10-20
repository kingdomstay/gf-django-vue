<template>
  <div id="app">
    <v-app>
      <AppBar/>
      <v-main>
        <router-view></router-view>
      </v-main>
      <Footer/>
    </v-app>
  </div>
</template>

<style lang="scss">

</style>

<script>
import Footer from "./components/Footer";
import AppBar from "./components/AppBar";
export default {
  components: {AppBar, Footer}
}
</script>
