<template>
  <v-app-bar
      app
      color="brown"
  >
    <v-container>

      <v-row
          align="center"
          justify="space-between"
      >
        <v-app-bar-title>
          <h3 class="text-h4 white--text">G&F</h3>
        </v-app-bar-title>
        <div>
          <v-btn class="deep-orange darken-1 white--text mx-1" depressed>
            Главная
          </v-btn>
          <v-btn class="white black--text mx-1" depressed>
            Меню
          </v-btn>
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
