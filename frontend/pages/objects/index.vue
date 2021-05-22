<template>
  <div class="container" style="margin-top:25px">
    <h1> Спортивный объекты </h1>
    <hr>

    <div class="object_block">

      <div class="object_block_1 zoom">
        <NuxtLink to="/objects/id" class="non_decoration">
          <div>
            <h2>Коробка</h2>
            <hr>
            <h3> ул Удмуртска 23</h3>
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
  width: 100%;
  padding: 2%;
  border-radius: 25px;
  background: #f5f5f5;
}

</style>