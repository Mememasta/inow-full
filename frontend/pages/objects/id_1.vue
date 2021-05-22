<template>
  <div class="container" style="margin-top:25px">
    <h1> Футбольная площадка </h1>
    <hr>

    <div class="flex object_block">

      <div class="object_block_text">
        <div class="object_block_text_1">
          <h4> Описание: площадка для игры в футбол </h4>
          <h4> Режим работы: 08:00 - 22:00 </h4>
          <h4> Вход: Свободный </h4>
          <h4> Адрес: Новый Уренгой, 4-й микрорайон  </h4>
        </div>
      </div>
      <div class="object_block_img">
        <img src="../../assets/img/football.jpg" width="80%" style="margin-left:15%;">
      </div>

    </div>

    <div class="">
      <img src="../../assets/img/map_sport_object.png" width="80%" style="margin:3% 10%">
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
  width: 100%;
  padding: 2%;
  border-radius: 25px;
  background: #defcf7;
}

.object_block_text{
  width: 50%;
  padding: 2%;
  position: relative;
}

.object_block_text_1{
  position: absolute;
  top: 25%;
}

.object_block_img{
  width: 50%;
  padding: 2%;
}

@media (max-width:565px){
  .object_block_text{
    width: 100%;
    padding: 2%;
    position: relative;
  }
  .object_block_text_1{
    position: relative;
    top: 0%;
  }
  .object_block_img{
    width: 100%;
    padding: 2%;
    margin-right: 10%;
  }
}

img{
  border-radius: 25px;
}

</style>