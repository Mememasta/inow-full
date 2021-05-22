<template>
  <div class="container" style="margin-top:25px">
    <h1> Лыжный марафон </h1>
    <hr>

    <div class="flex ">

      <div class="object_block">
        <h4>
           <span class="underline">Описание:</span> Лыжный марафон посвещен выдающийся советской лыжнице Галине Кулаковой.
           Участники пробегут 10 км. Победители получат ценные призы от администрации города.
           Участвовать могут как девушки, так и мужчины. Старт запланирован на 9 утра.
           На трассе будет горячий чай и обед.
        </h4>
        <br>
        <h4> <span class="underline">Дата:</span> 21.12.2021  </h4>
        <h4> <span class="underline">Время проведения:</span> 08:00 - 22:00 </h4>
        <h4> <span class="underline">Вход:</span> Свободный </h4>
        <h4> <span class="underline">Адрес:</span> Новый Уренгой, 4-й микрорайон  </h4>
        <h4> <span class="underline">Контакты:</span> +7 (978) 189-55-73 (Алена Одинцова)  </h4>
        <br>
        <b-button variant="outline-primary">Участвовать!</b-button>
      </div>

      <div class="">
        <img src="../../assets/img/ski_event.jpg" width="80%" style="margin:3% 10%">
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

</style>