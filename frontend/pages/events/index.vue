<template>
  <div class="container" style="margin-top:25px">
    <h1> Спортивные мероприятия </h1>
    <hr>

    <div class="events_block">

      <div class="events_block_1 zoom">
        <NuxtLink to="/events/id" class="non_decoration">
          <div>
            <h2>Лыжный марафон</h2>
            <hr>
            <h3> 21.12.2021</h3>
          </div>
        </NuxtLink>
      </div>


    </div>
   
  </div>
</template>


<script>
export default {
    layout: "MainLayout",
    head: {
        title: 'Главная',
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
  background: #f5f5f5;
}

</style>