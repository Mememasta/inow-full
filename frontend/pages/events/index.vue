<template>
  <div class="container" style="margin-top:25px">
    <div class="flex">
      <div class="name_block">
        <h1> Спортивные мероприятия. Новый Уренгой </h1>
      </div>
      <div class="add_block">
        <NuxtLink to="/events/add" class="non_decoration">
          <h1> &#10010; </h1>
        </NuxtLink>
      </div>
    </div>
    <hr>

    <div class="events_block">

      <div class="events_block_1 zoom">
        <NuxtLink to="/events/id_1" class="non_decoration">
          <div>
            <h2>Лыжный марафон</h2>
            <hr>
            <h3> 21.12.2021, 08:00 - 22:00, Новый Уренгой, 4-й микрорайон </h3>
          </div>
        </NuxtLink>
      </div>

      <div class="events_block_1 zoom">
        <NuxtLink to="/events/id_2" class="non_decoration">
          <div>
            <h2>Чемпионат города по баскетболу</h2>
            <hr>
            <h3> 18.05.2022 - 29.06.2022, Новый Уренгой, 2-й микрорайон </h3>
          </div>
        </NuxtLink>
      </div>

      <div v-for="event in events" :key="event.id" class="events_block_1 zoom">
        <NuxtLink :to="`/events/${event.id}`" class="non_decoration">
          <div>
            <h2>{{ event.name }}</h2>
            <hr>
            <h3> 
                {{
                    new Date(event.event_date).toLocaleDateString("ru-RU")
                }}
                -
                {{ 
                    new Date(event.event_date).getHours() + ":" + new Date(event.event_date).getMinutes()
                }}
            </h3>
            <h4>Участников: {{ event.members.length }}</h4>
          </div>
        </NuxtLink>
      </div>


    </div>
   
  </div>
</template>


<script>
export default {
    layout: "MainLayout",
    middleware: "auth",
    head: {
        title: 'Мероприятия',
    },
    data() {
        return {
            events: [],
            errors: []
        }
    },
    created() {
        this.$axios.get("/event").then(response => {
            this.events = response.data
        })
        .catch(e => {
            this.error.push(e)
        })
    }
  }
</script>


<style  scoped>

.events_block{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  top: 0;
  bottom: 0;
}

.events_block_1{
  width: 100%;
  padding: 2%;
  border-radius: 25px;
  background: #defcf7;
  margin-bottom: 2%;
}


.name_block{
  width: 90%;
}

.add_block{
  width: 10%;
}


@media (max-width:565px){
  .events_block_1{
    margin-bottom: 5%;
  }
  .name_block{
    width: 100%;
  }

  .add_block{
    width: 100%;
  }
}

</style>
