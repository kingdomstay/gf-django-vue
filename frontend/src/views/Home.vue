<template>
  <div>
    <v-carousel v-model="model">
      <v-carousel-item
          v-for="(color, i) in colors"
          :key="color"
      >
        <v-sheet
            :color="color"
            height="100%"
            tile
        >
          <v-row
              class="fill-height"
              align="center"
              justify="center"
          >
            <div class="text-h2">
              Slide {{ i + 1 }}
            </div>
          </v-row>
        </v-sheet>
      </v-carousel-item>
    </v-carousel>

    <v-container>
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
    </v-container>

    <v-container>
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
  </div>
</template>

<script>
export default {
  name: 'Home',
  data: () => ({
    model: 0,
    colors: [
      'primary',
      'secondary',
      'yellow darken-2',
      'red',
      'orange',
    ],
  }),
}
</script>
