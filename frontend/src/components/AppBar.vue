<template>
  <v-app-bar
      app
      color="brown darken-3"
  >
    <v-container>

      <v-row
          align="center"
          justify="space-between"
      >
        <v-app-bar-title>
          <v-img src="@/assets/logo.svg"></v-img>
        </v-app-bar-title>
        <div>
          <router-link to="/" v-slot="{href, isExactActive, navigate}">
            <v-btn @click="navigate" :href="href" :class="[isExactActive && 'deep-orange darken-1 white--text']" class="black--text mx-1" depressed>
              Главная
            </v-btn>
          </router-link>
          <router-link to="menu" v-slot="{href, isExactActive, navigate}">
            <v-btn @click="navigate" :href="href" :class="[isExactActive && 'deep-orange darken-1 white--text']" class="black--text mx-1" depressed>
              Меню
            </v-btn>
          </router-link>
          <v-btn class="white black--text mx-1" depressed>
            Личный кабинет
          </v-btn>
          <v-btn class="white black--text mx-1" depressed>
            Контакты
          </v-btn>
        </div>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: "AppBar"
}
</script>

<style scoped>

</style>
