<template>
  <v-container class="mt-8">
    <h1>О кофейне</h1>
    <h2 class="text-center text-h5 font-weight-bold mb-4">Компания сейчас</h2>
    <v-row>
      <v-col
      cols="12"
      sm="4"
      >
        <v-img src="@/assets/about_hero.png"></v-img>
      </v-col>
      <v-col>
        <p style="font-size: 1.4rem">
          “Гвоздика и Филин”  — это отличные люди, превосходный кофе и гостеприимная атмосфера
          В основе философии “G&F” лежит любовь к людям, и всё, что мы делаем, нацелено на то, чтобы каждый человек мог чувствовать себя непринужденно и комфортно, приходя к нам в гости
          13 кофеен по Москве - выбирай любую!
          “Гвоздика & Филин” - стабильно развивающийся бренд, основанный на сочетании отличных идей, грамотных управленческих решений и стремлении быть лучшими в своем деле. Мы готовы помочь нашим единомышленникам построить устойчивый и перспективный бизнес под эгидой проверенного временем бренда.
        </p>
      </v-col>
    </v-row>
    <h2 class="text-center text-h5 font-weight-bold mb-6 mt-10">Расположение кофеен</h2>
    <v-row>
      <v-col
        cols="12"
        sm="3"
        v-for="item in locations" :key="item.id"
        >
        <v-card
            class="mx-auto"
            max-width="400"
        >
          <v-img
              class="align-end text-white"
              height="200"
              :src="item.photo"
              cover
          >
            <v-card-title class="white--text">{{item.name}}</v-card-title>
          </v-img>

          <v-card-text>
            <div>{{item.address}}</div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "About",
  data: () => ({
    locations: ''
  }),
  mounted() {
    axios
        .get("http://127.0.0.1:8000/api/location/")
        .then(response => {
          this.locations = response.data;
        });
  }
}
</script>

<style scoped>

</style>
