<template>
  <div v-if="us" class="container" style="margin-top:25px">
    <h1> {{us.first_name}} {{us.second_name}} </h1>
    <hr>

    <h4> Телефон: {{ us.phone_number }} </h4>
    <h4> Баллы: 25&#9733; </h4>
    <h4> Почта: {{ us.email }} </h4>
   
  </div>
</template>


<script>
export default {
    layout: "MainLayout",
    middleware: 'auth',
    data() {
        return {
            us: null,
        }
    },
    created() {
        this.$axios.get('/user/' + this.$route.params.id).then(response => (this.us = response.data))
    },
    head: {
        title: 'Главная',
    }
  }
</script>

<style  scoped>

</style>
