<template>
  <v-container class="mt-8">

    <h1>Меню кофейни</h1>

    <v-row v-for="item in menu" :key="item.id">
      <v-col
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
            <v-chip class="orange darken-4 white--text"><h3>{{ item.price }} ₽</h3></v-chip>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <h1>Меню кофейни</h1>
      <h2 class="text-h4 my-4">Сезонное меню</h2>
      <v-row>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

      <h2 class="text-h4 my-4">Классическое меню</h2>
      <v-row>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col
            cols="12"
            sm="4"
        >
          <v-card>
            <v-img
                height="250"
                src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            ></v-img>
            <v-card-title>Капучино</v-card-title>
            <v-card-text>
              <div>Итальянский напиток, состоящий из Эспрессо, слоя взбитого молока и слоя молочной пенки.</div>
            </v-card-text>
            <v-divider class="mx-4"></v-divider>
            <v-card-text>
              <v-chip class="orange darken-4 white--text"><h3>199 ₽</h3></v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>

  </v-container>
</template>
<script>
import axios from "axios";

export default {
  name: "Menu",
  data() {
    return {
      menu: null
    };
  },
  mounted() {
    axios
        .get("http://127.0.0.1:8000/api/drink/")
        .then(response => (this.menu = response.data));
  }
}
</script>