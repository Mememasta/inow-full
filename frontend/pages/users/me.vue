<template>
  <div class="container" style="margin-top:25px">
    <h1> {{loggedInUser.first_name}} {{loggedInUser.second_name}} </h1>
    <hr>

    <h4> Телефон: {{ loggedInUser.phone_number }} </h4>
    <h4> Баллы: 25&#9733; </h4>
    <h4> Почта: {{ loggedInUser.email }} </h4>

   
  </div>
</template>


<script>
import { mapGetters } from 'vuex'
export default {
    layout: "MainLayout",
    middleware: 'auth',
    computed: {
        ...mapGetters(['loggedInUser'])
    },
    head: {
        title: 'Главная',
    }
  }
</script>

<style  scoped>

</style>
