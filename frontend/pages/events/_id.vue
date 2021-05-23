<template>
  <div v-if="event" class="container" style="margin-top:25px">
    <h1> Лыжный марафон </h1>
    <hr>

    <div class="flex ">

      <div class="object_block">
        <h4>
           <span class="underline">Описание:</span>
            {{ event.description }}
           
          
         
        </h4>
        <br>
        <h4> <span class="underline">Дата:</span> {{ new Date(event.event_date).toLocaleDateString("ru-RU")}}</h4>
        <h4> <span class="underline">Время проведения:</span>
            {{ new Date(event.event_date).getHours() + ":" + new Date(event.event_date).getMinutes() }}
        </h4>
        <h4> <span class="underline">Контакты:</span> {{ event.organizer.phone_number }} {{ event.organizer.first_name }}  </h4>
        <h4> <span class="underline">Участников:</span> {{ event.members.length }}</h4>
        <br>
        <b-button  @click="toParticipate" variant="outline-primary">Участвовать!</b-button>
    
      </div>

      <div v-if="event.photo_path" class="">
        <img :src="event.photo_path" width="80%" style="margin:3% 10%;">
      </div>


    </div>
   
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    layout: "MainLayout",
    middleware: 'auth',
    data() {
        return {
            event: null,
            errors: []
        }
    },
    created() {
        this.$axios.get('/event/' + this.$route.params.id).then(response => (this.event = response.data))
    },
    computed: {
        ...mapGetters(['loggedInUser'])
    },
    methods: {
        async toParticipate() {
            await this.$axios.get("/event/to_participate/" + this.$route.params.id)
            .then(response => {
                this.event = response.data
            })
            .catch(e => {
                this.errors.push(e)
            })
        }
    },
    head: {
        title: 'Главная',
    }
  }
</script>

<style  scoped>
.underline{
  text-decoration: underline;
}

.object_block{
  width: 100%;
  padding: 2%;
  border-radius: 25px;
  background: #defcf7;
}

img{
  border-radius: 25px;
}
</style>
