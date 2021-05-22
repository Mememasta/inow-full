<template>
  <div class="container" style="margin-top:25px">
    <h1> Чемпионат города по баскетболу </h1>
    <hr>

    <div class="flex">

      <div class="object_block">
        <h4>
           <span class="underline">Описание:</span> Нас ожидает полтора месяца интересных соревнований по баскетболу. 
           Вы можете зарегестрировать свою команду, состоящую из 6 человек, позвонив нашему координатору.
           Игры будут проходить на современнных площадках, а судить будут профессионалы.
           Обязательное требование - это единая форма у команды!
        </h4>
        <br>
        <h4> <span class="underline">Дата:</span> 18.05.2022 - 29.06.2022  </h4>
        <h4> <span class="underline">Время проведения:</span> 16:00 - 21:00 </h4>
        <h4> <span class="underline">Адрес:</span> Новый Уренгой, 2-й микрорайон  </h4>
        <h4> <span class="underline">Контакты:</span> +7 (978) 189-55-73 (Алена Одинцова)  </h4>
        <br>
        <b-button variant="outline-primary">Участвовать!</b-button>
      </div>

      <div class="">
        <img src="../../assets/img/basket_object.png" width="80%" style="margin:3% 10%">
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