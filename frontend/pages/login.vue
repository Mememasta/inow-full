<template>
    <div
        class="card container form-signin text-center"
        style="width: 30em; border-radius: 15px"
    >
        <Notification :message="error" v-if="error"/>
        <b-form @submit.prevent="login" v-if="show">
            <h1 class="h3 m-4 font-weight-normal">Вход</h1>

            <b-form-group id="email" label-for="email">
                <b-form-input
                    id="email"
                    v-model="email"
                    type="email"
                    required
                    placeholder="Введите email"
                ></b-form-input>
            </b-form-group>

            <b-form-group id="password" label-for="password">
                <b-form-input
                    id="password"
                    v-model="password"
                    type="password"
                    required
                    placeholder="Введите пароль"
                ></b-form-input>
            </b-form-group>

            <b-button type="submit" variant="primary" block>Войти</b-button>

            <br />

            <NuxtLink to="/signup">Регистрация</NuxtLink> |
            <NuxtLink to="/">Главная</NuxtLink>
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
          password: '',
          show: true,
          error: '',
        };
    },
    methods: {
        async login() {
          try {
            const params = new URLSearchParams();
            params.append('username', this.email);
            params.append('password', this.password);
            await this.$auth.loginWith('local', {
              data: params
            })

            this.$nuxt.$router.replace({ path: '/'})
          } catch (e) {
            this.error = e.response.data.detail
          }
        }
    }
  }
</script>
