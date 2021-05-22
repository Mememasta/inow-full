<template>
  <div class="container" style="margin-top:25px">
    <h1> Все работники </h1>
    <hr>

    <div class="margin_block">
      <b-button v-b-toggle.collapse-1 class="block_task">
        <h4> Офис </h4>
      </b-button>
      <b-collapse id="collapse-1" class="mt-2">
        <b-card>         
          <table class="iksweb">
            <thead>
            <tr>
              <th>Имя Фамилия<br></th>
              <th>Должность</th>
              <th class="table_phone">Написать</th>
              <th class="table_phone">Контакт</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td><Nuxt-link to="/users"> Никита Русских </Nuxt-link></td>
              <td>Пограммист</td>
              <td class="table_phone"><Nuxt-link to="/messages"> Мессенджер </Nuxt-link></td>
              <td class="table_phone"> +7 (964)-180-87-81</td>
            </tr>
            <tr>
              <td><Nuxt-link to="/users"> Марат Чучалов </Nuxt-link></td>
              <td>Главный программист</td>
              <td class="table_phone"><Nuxt-link to="/messages"> Мессенджер </Nuxt-link></td>
              <td class="table_phone">  +7 (909)-180-87-81</td>
            </tr>
            </tbody>
          </table>
        </b-card>      
      </b-collapse>
    </div>

    <div class="margin_block">
      <b-button v-b-toggle.collapse-2 class="block_task">
        <h4> Склад </h4>
      </b-button>
      <b-collapse id="collapse-2" class="mt-2">
        <b-card>         
          <table class="iksweb">
            <thead>
            <tr>
              <th>Имя Фамилия<br></th>
              <th>Должность</th>
              <th class="table_phone">Написать</th>
              <th class="table_phone">Контакт</th>
            </tr>
            </thead>
            <tbody>
            <tr>
              <td><Nuxt-link to="/users"> Арсений Круглый </Nuxt-link></td>
              <td>Грузчик</td>
              <td class="table_phone"><Nuxt-link to="/messages"> Мессенджер </Nuxt-link></td>
              <td class="table_phone"> +7 (964)-180-87-81</td>
            </tr>
            <tr>
              <td><Nuxt-link to="/users"> Григорий Павлов </Nuxt-link></td>
              <td>Уборщик</td>
              <td class="table_phone"><Nuxt-link to="/messages"> Мессенджер </Nuxt-link></td>
              <td class="table_phone">  +7 (909)-180-87-81</td>
            </tr>
            </tbody>
          </table>
        </b-card>      
      </b-collapse>
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
.margin_block{
  margin-bottom: 3%;
}
.block_task {
  padding: 1%;
  background: #f5f5f5;
  border-radius: 20px;
  color: black; 
  border: 0px; 
  width: 100%
}

/* Стили таблицы (IKSWEB) */
table.iksweb{text-decoration: none;border-collapse:collapse;width:100%;text-align:center;}
table.iksweb th{font-weight:normal;font-size:16px; color:#000;background-color:#9cd6ff;}
table.iksweb td{font-size:14px;color:#000;}
table.iksweb td,table.iksweb th{white-space:pre-wrap;padding:16px 10px;line-height:14px;vertical-align: middle;border: 0px solid #61b0e8;}	table.iksweb tr:hover{background-color:#daf7ea}
table.iksweb tr:hover td{color:#000;cursor:pointer;}

@media (max-width:769px){
    .table_phone {
        display: none;
    }
}
</style>