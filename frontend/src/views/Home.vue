<template>
  <div>
    <v-carousel v-model="model">
      <v-carousel-item
          v-for="post in news"
          :key="post.id"
      >
        <v-sheet
            height="100%"
            tile
        >
          <v-row
              class="fill-height"
              align="center"
              justify="center"
          >
            <v-img style="position: absolute; left: 0; top: 0; width: 100%; height: 100%; object-fit: cover;" :src="post.photo"></v-img>
            <div class="text-h2" style="z-index: 2">
              <router-link :to="{ name: 'news', params: { id: post.id } }">{{post.title}}</router-link>
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-container>
      <h1 class="my-4">Меню кофейни</h1>
      <v-row>
        <v-col
            v-for="item in menu" :key="item.id"
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                :src="item.photo"
            ></v-img>
            <v-card-title>{{ item.title }}</v-card-title>
            <v-card-text>
              <div>{{ item.description }}</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text mx-1"><h3>{{ item.price }} ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-container>
      <h2 class="text-center text-h4 mt-10">О компании:</h2>
      <v-row class="my-4">
        <v-col>
          <p style="font-size: 1.5rem">
            “Гвоздика и Филин”  — это отличные люди, превосходный кофе и гостеприимная атмосфера
            В основе философии “G&F” лежит любовь к людям, и всё, что мы делаем, нацелено на то, чтобы каждый человек мог чувствовать себя непринужденно и комфортно, приходя к нам в гости
            13 кофеен по Москве - выбирай любую!
            “Гвоздика & Филин” - стабильно развивающийся бренд, основанный на сочетании отличных идей, грамотных управленческих решений и стремлении быть лучшими в своем деле. Мы готовы помочь нашим единомышленникам построить устойчивый и перспективный бизнес под эгидой проверенного временем бренда.
          </p>
          <router-link to="about">
            <v-btn color="primary">Узнать больше</v-btn>
          </router-link>
        </v-col>
        <v-col>
          <v-img src="@/assets/about_banner.png"></v-img>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Home',
  data: () => ({
    news: null,
    model: 0,
    colors: [
      'primary',
      'secondary',
      'yellow darken-2',
      'red',
      'orange',
    ],
    menu: []
  }),
  mounted() {
    axios.get("http://127.0.0.1:8000/api/news/")
        .then(response => (this.news = response.data))
    axios
        .get("http://127.0.0.1:8000/api/drink/")
        .then(response => {
          this.menu = response.data;
        });
  }
}
</script>
