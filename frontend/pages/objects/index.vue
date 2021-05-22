<template>
  <div class="container" style="margin-top:25px">
    <h1> Спортивный объекты. Новый Уренгой </h1>
    <hr>

    <div class="object_block">

      <div class="object_block_1 zoom">
        <NuxtLink to="/objects/id_1" class="non_decoration">
          <div>
            <h2> Футбольная площадка </h2>
            <hr>
            <h4> Новый Уренгой, 4-й микрорайон </h4>
          </div>
        </NuxtLink>
      </div>

      <div class="object_block_1 zoom">
        <NuxtLink to="/objects/id_1" class="non_decoration">
          <div>
            <h2>Баскетбольная площадка</h2>
            <hr>
            <h4> Новый Уренгой, 3-й микрорайон </h4>
          </div>
        </NuxtLink>
      </div>


      <div class="object_block_1 zoom">
        <NuxtLink to="/objects/id_1" class="non_decoration">
          <div>
            <h2>Воркаут</h2>
            <hr>
            <h4> Новый Уренгой, микрорайон Оптимистов </h4>
          </div>
        </NuxtLink>
      </div>


      <div class="object_block_1 zoom">
        <NuxtLink to="/objects/id_1" class="non_decoration">
          <div>
            <h2>Хоккейная площадка</h2>
            <hr>
            <h4> Новый Уренгой, 1-й микрорайон</h4>
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

.object_block{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  top: 0;
  bottom: 0;
}

.object_block_1{
  width: 48%;
  padding: 2%;
  border-radius: 25px;
  background: #defcf7;
  margin: 1%;
}

</style>