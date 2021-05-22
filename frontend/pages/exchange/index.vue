<template>
  <div class="container" style="margin-top:25px">
    <h1> Аренда от людей </h1>
    <hr>

    <div class="exchange_block">

      
      <div class="exchange_block_1">
        <h3>Аренда лыж</h3>
        <hr>
        <img src="../../assets/img/fischer.jpeg" width="100%">
        <br>
        <br>
        <h3>Нина Иванова</h3>
        <h4>Телефон: +7 (948) 452-78-93</h4>
        <h4>Цена: 250 рублей за 1 час</h4>
        <h4>Описание: Лыжи Fischer, парафин на -10 градусов</h4>
      </div>

      <div class="exchange_block_1">
        <h3>Аренда велосипеда</h3>
        <hr>
        <img src="../../assets/img/rent_by.jpg" width="100%">
        <br>
        <br>
        <h3>Алексей Филатов</h3>
        <h4>Телефон: +7 (957) 154-78-48</h4>
        <h4>Цена: 150 рублей за 1 час</h4>
        <h4>Описание: Велосипед Forward, в идеальном состоянии, дисковые тормоза</h4>
      </div>

      <div class="exchange_block_1">
        <h3>Аренда лыж</h3>
        <hr>
        <img src="../../assets/img/fischer.jpeg" width="100%">
        <h4>250 рублей за 2 часа</h4>
        <div>

          <h5> Время начала аренды </h5>
          <b-form-timepicker v-model="value" locale="en"></b-form-timepicker>

          <h5> Время окончания аренды </h5>
          <b-form-timepicker v-model="value_1" locale="en"></b-form-timepicker>

          <b-button>Забронировать</b-button>

        </div>
      </div>  

      <div class="exchange_block_1">
        <h3>Аренда велосипеда</h3>
        <hr>
        <img src="../../assets/img/rent_by.jpg" width="100%">
        <h4>150 рублей за 2 часа</h4>
        <div>

          <h5> Время начала аренды </h5>
          <b-form-timepicker v-model="value" locale="en"></b-form-timepicker>

          <h5> Время окончания аренды </h5>
          <b-form-timepicker v-model="value_1" locale="en"></b-form-timepicker>

          <b-button>Забронировать</b-button>

        </div>
      </div>  



    </div>
   
  </div>
</template>


<script>
export default {
    layout: "MainLayout",
    head: {
        title: 'Главная',
    },
    data() {
      return {
        value: '',
        value_1: '',
      }
    }
  }
</script>

<style  scoped>

.exchange_block{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  top: 0;
  bottom: 0;
}

.exchange_block_1{
  margin:  1%;
  width: 48%;
  padding: 2%;
  border-radius: 25px;
  background: #f5f5f5;
}

@media (max-width:565px){
  .exchange_block_1{
    width: 100%;
    padding: 2%;
    border-radius: 25px;
    background: #f5f5f5;
  }
}


img{
  border-radius: 25px;
}

</style>