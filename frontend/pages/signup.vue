<template>
    <div class="card container form-signin text-center" style="width: 40em; border-radius: 15px">
        <Notification :message="error" v-if="error"/>
        <b-form @submit.prevent="register" v-if="show">
            <h1 class="h3 m-4 font-weight-normal">Регистрация</h1>
            <b-form-group
                id="email"
                label-for="email"
            >
            <b-form-input
                id="email"
                v-model="email"
                type="email"
                required
                placeholder="Введите email"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="phone_number"
                label-for="phone_number"
            >
            <b-form-input
                id="phone_number"
                v-model="phone_number"
                type="tel"
                required
                placeholder="Введите номер телефона"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="password"
                label-for="password"
            >
            <b-form-input
                id="password"
                v-model="password"
                type="password"
                required
                placeholder="Введите пароль"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="second_name"
                label-for="second_name"
            >
            <b-form-input
                id="second_name"
                v-model="second_name"
                type="text"
                required
                placeholder="Введите фамилию"
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="first_name"
                label-for="first_name"
            >
            <b-form-input
                id="first_name"
                v-model="first_name"
                type="text"
                required
                placeholder="Введите имя"
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary" block>Зарегистрироваться</b-button>
            
            <br>

            <NuxtLink to="/login">У меня есть профиль</NuxtLink> | <NuxtLink to="/">Главная</NuxtLink>
            <p class="mt-3 mb-3 text-muted">&copy; 2021</p>

        </b-form>
    </div>
</template>

<script>
  export default {
    middleware: 'quest',
    layout: "LoginLayout",
    data() {
      return {
          email: '',
          phone_number: '',
          password: '',
          first_name: '',
          second_name: '',
          show: true,
          error: ''
        };
    },
    methods: {
        async register() {
          try {
            await this.$axios.post('user/open/create', {
                email: this.email,
                phone_number: this.phone_number,
                password: this.password,
                first_name: this.first_name,
                second_name: this.second_name,
            })
            const params = new URLSearchParams();
            params.append('username', this.email);
            params.append('password', this.password);
            await this.$auth.loginWith('local', {
              data: params
            })

            this.$nuxt.$router.replace({ path: '/'})
          } catch (e) {
            this.error = e.response
          }
        }
    }
  }
</script>
