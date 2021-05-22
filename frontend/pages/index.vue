<template>
  <div class="">
    
    <div class="first_block">

      <div class="first_block_name">
        <h1 class="first_block_name_title">ЯНАО-Спорт</h1>
      </div>

      <div class="first_block_img">
        <img src="../assets/img/bicycle.png" width="100%">
      </div>
        
    </div>
    


    <div class="second_block">

      <div class="second_block_img">
        <img src="../assets/img/bicycle.png" width="100%">
      </div>

      <div class="second_block_description">
        <h3 class="" style="color:white;">
          Данная плаформа создана для развития спорта в Ямало-Ненецкого автономного округа.
          Здесь вы можете арендовать спортивное оборудование, узнать о мероприятиях и поучавтсвовать в соревнованиях.
        </h3>
      </div>

    </div>


    <div class="you_may">

      <div class="you_may_head">
        <h1> У нас на площадке можно: </h1>
      </div>

      <div class="body">
        <div class="you_may_blocks_left">
          <h1> 1</h1>
        </div>

      </div>

      <div class="body">

        <div class="you_may_blocks_right">
          <h1> 2 </h1>
        </div>
      
      </div>
    </div>

      




        

    <div class="sig_log">

      <div class="card container form-signin text-center" style="width: 30em; border-radius: 15px">
        <b-form >
            <h1 class="h3 m-4 font-weight-normal">Вход</h1>

            <b-form-group id="email" label-for="email">
                <b-form-input
                    id="email"
                    v-model="form.username"
                    type="email"
                    required
                    placeholder="Введите email"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="password" label-for="password">
                <b-form-input
                    id="password"
                    v-model="form.password"
                    type="password"
                    required
                    placeholder="Введите пароль"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-4">
                <b-form-checkbox-group v-model="form.checked" id="checkboxes-4">
                    <b-form-checkbox value="me">Запомнить</b-form-checkbox>
                </b-form-checkbox-group>
            </b-form-group>

            <b-button type="submit" variant="primary" block>Войти</b-button>

            <br />

        </b-form>
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
            form: {
                username: "",
                password: "",
                checked: [],
            },
            show: true,
        };
    },
    methods: {
        async onSubmit() {
            let username = this.form.username;
            let password = this.form.password;
            let checked = this.form.checked;
            this.$store.dispatch("accessToken", {
                username: username,
                password: password,
            });
        },
        async onReset() {
            // Reset our form values
            this.form.email = "";
            this.form.password = "";
            this.form.checked = [];
            // Trick to reset/clear native browser form validation state
            this.show = false;
            this.$nextTick(() => {
                this.show = true;
            });
        },
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
}

.first_block_name{
  width: 50%;
}

.first_block_img{
  width: 50%;
}

.first_block_name_title{
  font-size: 72px;
  text-align: center;;
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

.second_block_description{
  width: 70%;
  padding: 0% 10%;
}

.second_block_img{
  width: 30%;
}

.sig_log{
  background: white;
  padding: 5% 0%;
}

.you_may {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-items: center;
  height: 100%;
  background-color: #c5dbb7;
  top: 0;
  bottom: 0;
}

.you_may_head{
  text-align: center;
  width: 100%;
}

.you_may_body{
  width: 100%;
}

.you_may_blocks_left{
  background: #2f32ce;
  width: 40%;
  margin-left: 20%;
}

.you_may_blocks_right{
  background: #b361e2;
  width: 40%;
  margin-left: 40%;
}

</style>
