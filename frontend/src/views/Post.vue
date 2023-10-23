<template>
<v-container>
  <v-img class="my-8" :src="post.photo"></v-img>
  <h1 class="mt-10 mb-4">{{post.title}}</h1>
  <p>{{post.description}}</p>
</v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Post",
  data: () => ({
    post: null
  }),
  mounted() {
    axios.get(`http://127.0.0.1:8000/api/news/${this.$route.params.id}`)
        .then(response => (this.post = response.data))
  }
}
</script>

<style scoped>

</style>
