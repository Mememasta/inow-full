<template class="gym-fon">
  <div class="container" style="margin-top:25px">
    <h1> Сервисы </h1>
    <hr>

    <div class="services_block">
    
      
      <div class="services_block_1 zoom">
        <NuxtLink to="/services/rent_bicycle/" class="non_decoration">
          <div>
            <h2>Аренда велосипедов</h2>
            <hr>
            <h3>От 50 рублей</h3>
          </div>
        </NuxtLink>
      </div>
      

      <div class="services_block_1 zoom">
        <NuxtLink to="/services/rent_bicycle/" class="non_decoration">
          <div>
            <h2>Аренда самокат</h2>
            <hr>
            <h3>От 50 рублей</h3>
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
.gym-fon {
background: url(@/assets/img/gym-fon.png) center/cover no-repeat;
    background-size: cover;
-webkit-background-size: cover;
-moz-background-size: cover;
-o-background-size: cover;
background-size: cover;}

.services_block{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  top: 0;
  bottom: 0;
}

.services_block_1{
  margin:  1%;
  width: 48%;
  padding: 2%;
  border-radius: 25px;
  background: #defcf7;
}

@media (max-width:565px){
  .services_block_1{
    width: 100%;
    padding: 2%;
    border-radius: 25px;
    background: #defcf7;
  }
}


</style>