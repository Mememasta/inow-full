<template>
  <div class="">
    
    <div class="first_block">

      <div class="first_block_name">
        <h1 class="first_block_name_title">ЯНАО-Спорт</h1>
      </div>

      <div class="first_block_img">
        <img src="../assets/img/gerb.png" width="40%" style="margin-left:30%;">
      </div>
        
    </div>
    


    <div class="second_block">

        <h3 class="second_block_head">
          Данная платформа создана для развития спорта в Ямало-Ненецком автономном округе.
        </h3>

    </div>




    <div class="you_may">

      <div class="you_may_head">
        <h1 class="phone_text"> У нас на площадке вы можете: </h1>
      </div>

      
      <div class="you_may_blocks zoom">
          <NuxtLink to="/events" class="non_decoration">
          <h2 class="phone_text"> 1. Узнать о спортивных мероприятиях </h2>
          </NuxtLink>
      </div>
      

      
      <div class="you_may_blocks zoom">
        <NuxtLink to="/objects" class="non_decoration">
          <h2 class="phone_text"> 2. Узнать о нахождениях и расписании спортивных объектов </h2>
        </NuxtLink>
      </div>
      

      
      <div class="you_may_blocks zoom">
        <NuxtLink to="/exchange" class="non_decoration">
          <h2 class="phone_text"> 3. Арендовать спортивный инвертарь у людей или сдать свой </h2>
        </NuxtLink>
      </div>
      

    </div>


    <div class="bus_and_people">
      <div class="people">
        <h2 class="bus_and_people_head"> Для пользователей </h2>
        <h4> 1. Возможность заниматься спортом </h4>
        <h4> 2. Получать актуальную информацию </h4>
      </div>
      <div class="bus">
        <h2 class="bus_and_people_head"> Для бизнеса </h2>
        <h4> 1. Возможность разместить товар на площадке </h4>
        <h4> 2. Привлечение клиентов </h4>
      </div>
    </div>   

      




        

    <div class="sig_log_block">

      <div class="sig_log_head_block">
        <h1 class="sig_log_head"> Спорт - это жизнь. </h1>
        <h1 class="sig_log_head"> Присоединяйся к нам прямо сейчас! </h1>
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
}
</script>

<style>


.first_block {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  background-color: #f1f1f3;
  top: 0;
  bottom: 0;
  padding: 2%;
}

.first_block_name{
  width: 50%;
}

.first_block_img{
  width: 50%;
}

.first_block_name_title{
  font-size: 86px;
  text-align: right;
}

@media (max-width:565px){
  .first_block_name{
    width: 100%;
  }
  .first_block_img{
    width: 100%;
  }
  .first_block_name_title{
    font-size: 42px;
    text-align: center;
  }
}



.second_block {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  background-color: #7070ce;
  top: 0;
  bottom: 0;
}

.second_block_head{
  padding: 5%;
  color: white;
  font-size: 32px;
  text-align: center;
}

@media (max-width:565px){
  .second_block_head{
    padding: 5%;
    font-size: 24px;
    
  }
}



.you_may {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  height: 100%;
  background-color: #f5f5f5;
  top: 0;
  bottom: 0;
  padding: 4%;
}

.you_may_head{
  text-align: center;
  width: 100%;
  padding: 0% 0% 2% 0%;
}

.you_may_blocks{
  text-align: center;
  background: #cef3e4;
  width: 70%;
  padding: 1%;
  margin-left: 15%;
  margin-bottom: 1%;
  border-radius: 25px;
}

@media (max-width:565px){
  .you_may_blocks{
    width: 90%;
    padding: 4%;
    margin-left: 5%;
    margin-bottom: 5%;
    border-radius: 25px;
  }
  .phone_text{
    font-size: 24px;
  }
}




.bus_and_people{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  height: 100%;
  top: 0;
  bottom: 0;
}

.bus{
  width: 50%;
  background: #ebe6b9;
  text-align: center;
  padding: 2%;
}

.people{
  width: 50%;
  background: #e9bdd8;
  text-align: center;
  padding: 2%;
}

.bus_and_people_head{
  margin-bottom: 3%;
  text-decoration: underline;
}

@media (max-width:565px){
  .bus{
    width: 100%;
    background: #ebe6b9;
    text-align: center;
    padding: 2%;
  }
  .people{
    width: 100%;
    background: #e9bdd8;
    text-align: center;
    padding: 2%;
  }
  .bus_and_people_head{
    margin-bottom: 3%;
    text-decoration: underline;
  }
}


.sig_log_block{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  height: 100%;
  background-color: #f5f5f5;
  top: 0;
  bottom: 0;
  padding: 2%;
}

.sig_log{

}

.sig_log_head_block{
  width: 100%;
}

.sig_log_head{
  text-align: center;
}


@media (max-width:565px){
  .sig_log{
    display: none;
  }
  .sig_log_head_block{
    width: 100%;
  }
  .sig_log_head{
    text-align: center;
  }
}



</style>
